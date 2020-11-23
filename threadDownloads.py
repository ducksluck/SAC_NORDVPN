import urllib3
import os
from concurrent.futures import ThreadPoolExecutor


# globals are for progress bar.
global count, bar_progress, printed, sum_servers
count = 0
bar_progress = 1
printed = False


def downloadFile(url, colors):
    http = urllib3.PoolManager()
    filename = url.split("/")[-1]

    global bar_progress, count, sum_servers
    fullname = os.getcwd() + "\\ovpnConfigs\\" + filename
    fileexists = os.path.isfile(fullname)
    if not fileexists:
        response = http.request('GET', url, preload_content=False)
        file = open(fullname, "wb")
        file.write(response.data)
        file.close()

    # Progress bar logic
    if ((sum_servers / 100) * bar_progress) < count < ((sum_servers / 100) * (bar_progress + 1)):
        print("\x1b[%sm#\x1b[0m" % colors['color1'], end='')
        bar_progress += 1
    count += 1


# WARNING: Max_workers can be adjusted but if download limit is exceeded Nordvpn will serve up
#          a corrupt openvpn config with a warning message on purpose.
#          Corrupt file size is about 1kb instead of the standard 3k.
#          I found it was faster in the end to to push the limit and then at the end check for
#          small corrupt files and download those specific ones again. (see ReplaceCorrupt.py)

def threadDownloads(names_urls, x, colors):
    global sum_servers, printed, bar_progress, count
    sum_servers = len(names_urls)
    bar = "\x1b[%sm  0%s|----------------------------------------------------------------------------------------------------|100%s \x1b[0m" % (colors['color2'], '%', '%')
    print(bar)
    print("     ", end="")   # padding for progress
    bar_progress = 1
    count = 0
    printed = False

    # start threading
    futures_list = []
    results = []
    with ThreadPoolExecutor(max_workers=x) as executor:
        for url in names_urls:
            futures = executor.submit(downloadFile, url, colors)
            futures_list.append(futures)

        for future in futures_list:
            try:
                result = future.result(timeout=60)
                results.append(results)
            except Exception:
                results.append(None)

    # 100% print last '#'
    if bar_progress < 100:
        print("\x1b[%sm#\x1b[0m" % colors['color1'] * 100)
    else:
        print("\x1b[%sm#\x1b[0m" % colors['color1'])
