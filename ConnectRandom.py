import random
import os
from launchVPN import launchVPN


def ConnectRandom(configPoolDir, colors):
    configPool = os.listdir(configPoolDir)
    confCount = (len(configPool))
    randomServer = random.randrange(0, confCount)
    launchVPN(configPool[randomServer], configPoolDir, colors)
