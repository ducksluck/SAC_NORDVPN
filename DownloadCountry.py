from getLinks import getLinks
from RemoveOldConfigs import RemoveOldConfigs


def DownloadCountry(configPoolDir, colors):
    msg = "\x1b[%sm  Enter a two letter Country abbreviation: \x1b[0m " % colors['color1']
    selectedCountry = input(msg)
    if len(selectedCountry) > 2:
        print("\x1b[%sm Only two letter country abbreviations can be used. \x1b[0m" % colors['red_box'])
    else:
        RemoveOldConfigs(selectedCountry, configPoolDir, colors)
        getLinks(selectedCountry, configPoolDir, colors)

