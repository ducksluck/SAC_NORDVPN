from getLinks import getLinks
from RemoveOldConfigs import RemoveOldConfigs

# TODO figure out why the progress bar over runs for double vpn


def DownloadAllDoubles(configPoolDir, colors):
    RemoveOldConfigs("-", configPoolDir, colors)
    getLinks("-", configPoolDir, colors)
