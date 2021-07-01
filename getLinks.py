import requests
import time
from bs4 import BeautifulSoup as bs
from threadDownloads import threadDownloads
from ReplaceCorrupt import ReplaceCorrupt


def getLinks(abrv, configPoolDir, colors):

    # Select VPN config types
    print("\n\x1b[%sm  Select VPN Connection type: \x1b[0m \n" % colors['color_box1'])
    print("\t \x1b[%sm [1] \x1b[0m \x1b[%sm TCP configs \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    print("\t \x1b[%sm [2] \x1b[0m \x1b[%sm UDP configs \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    print("\t \x1b[%sm [3] \x1b[0m \x1b[%sm Both TCP & UDP \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    selectmsg = "\n \x1b[%sm  Select Connection Type: \x1b[0m " % colors['color_box1']
    tcp_udp = input(selectmsg)
    if tcp_udp == '1':
        tcp_udp = 'tcp443'
    elif tcp_udp == '2':
        tcp_udp = 'udp1194'
    elif tcp_udp == '3':
        tcp_udp = 'both'

    print("\n \x1b[%sm   Beginning scrape...\x1b[0m \n" % colors['color2'])
    sourceURL = 'https://nordvpn.com/ovpn/'
    r = requests.get(sourceURL)

    soup = bs(r.text, "html.parser")

    #  Selection logic: All, doubleVPNs, single country -- TCP and/or UDP
    abrvlen = len(abrv)
    tempURLS = []
    for i, link in enumerate(soup.findAll('a')):   
        _fullurl = link.get('href')
        if _fullurl is not None:
            if _fullurl.endswith('.ovpn'):  # ignore links that aren't opvn configs
                # Download All
                if abrv == "All":
                    if tcp_udp == 'both':                                                 # TCP -&- UDP
                            tempURLS.append(_fullurl)
                    else:                                                                 # TCP -or- UDP
                        if _fullurl.__contains__(tcp_udp):
                            tempURLS.append(_fullurl)

                # Filter Double VPNs
                elif abrv == "-":
                    if tcp_udp == 'both':
                        if "-" in _fullurl:
                            tempURLS.append(_fullurl)
                    if tcp_udp == 'tcp443':
                        if _fullurl.__contains__(tcp_udp) & _fullurl.__contains__("-"):
                            tempURLS.append(_fullurl)
                    if tcp_udp == 'udp1194':
                        if _fullurl.__contains__(tcp_udp) & _fullurl.__contains__("-"):
                            tempURLS.append(_fullurl)

                # Filter Single Country
                else:
                    rawname = _fullurl[25:].split("/")[-1].split(".")
                    name = rawname[0]
                    if tcp_udp == 'both':
                        if name[0:abrvlen] == abrv:
                            tempURLS.append(_fullurl)
                    else:
                        if name[0:abrvlen] == abrv :
                            if _fullurl.__contains__(tcp_udp):
                                tempURLS.append(_fullurl)

    # Prep for downloading, get 'max workers' if downloading all configs
    serversum = len(tempURLS)
    if serversum >= 1:
        dlmsg = "\x1b[%sm  Downloading %d config files\x1b[0m" % (colors['color2'], serversum)
        print(dlmsg)
        maxworkers = 30
        if abrv == "All":
            print("\n \x1b[%sm Adjust Threading:\x1b[0m" % colors['color1'])
            print("\x1b[%sm     Downloading all configs one at a time can easily take upwards of 30 mins even though they're small files.\x1b[0m" % colors['color2'])
            print("\x1b[%sm     You can try to adjust the thread count.\x1b[0m" % colors['color2'])
            print("\x1b[%sm     However, if download limit is reached configs will be corrupt, 1kb in size, and contain a warning message.\x1b[0m" % colors['color2'])
            print("\x1b[%sm     The recommended number of worker threads is 30.\x1b[0m" % colors['color2'])
            print("    \x1b[%sm Approx runtime with 30 workers (recommended) is 20 mins for all 10k+ configs \x1b[0m" % colors['red_box'])
            maxinput = int(input(" \x1b[%sm Max Workers ([Enter] for default 10): \x1b[0m " % colors['color1']) or "10")
            if maxinput == "":   # Default to '30' in case user presses enter
                pass
            else:
                maxworkers = int(maxinput)
            startTime = time.time()
            threadDownloads(tempURLS, maxworkers, colors)
        else:
            startTime = time.time()
            threadDownloads(tempURLS, maxworkers, colors)  # 30 maxworkers for doublevpn and single country

        # End timer and get runtime
        totaltime = time.time() - startTime
        mins = totaltime / 60
        mins = str(round(mins))
        seconds = str(totaltime % 60).split(".")[0]    # grab on the significant digits of the remainder.
        msg = "\x1b[%sm     Runtime was %s minutes and %s Seconds: \x1b[0m" % (colors['color2'], mins, seconds)
        print(msg)

        # Check for corrupt configs and download again.
        ReplaceCorrupt(configPoolDir, colors)

    else:
        print("  \x1b[%sm There are no available configs for that country code. \x1b[0n" % colors['red_box'])
