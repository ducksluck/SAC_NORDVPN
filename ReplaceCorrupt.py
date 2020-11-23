import os
from threadDownloads import threadDownloads


def ReplaceCorrupt(configPoolDir, colors):
    foundurls = []
    foundfiles = []

    for filename in os.listdir(configPoolDir):
        path = os.path.join(configPoolDir, filename)
        try:
            if filename[-5:] == ".ovpn":
                if os.stat(configPoolDir+filename).st_size < 2000:
                    url=("https://downloads.nordcdn.com/configs/files/ovpn_legacy/servers/" + filename)
                    foundurls.append(url)
                    foundfiles.append(filename)
                else:
                    pass
        except Exception as e:
            print('\x1b[%sm Failed %s. Error: %s \x1b[0m' % (colors['red_box'], path, e))

    if len(foundurls) != 0:
        checkmsg = "\n\x1b[%sm  Retrying %d corrupt config files\x1b[0m" % (colors['color2'], len(foundurls))
        print(checkmsg)
        for filename in foundfiles:
            path = os.path.join(configPoolDir, filename)
            try:
                os.remove(path)
            except Exception as e:
                print('\x1b[%sm  Failed to remove corrupt 1k config file: %s. Error: %s \x1b[0m' % (colors['red_box'], path, e))

        threadDownloads(foundurls, 10, colors)
