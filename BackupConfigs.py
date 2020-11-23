import shutil
import os


def BackupConfigs(configPoolDir, colors):

    bakPath = os.getcwd() + "\\configs.bak"

    shutil.make_archive(bakPath, 'zip', configPoolDir)
    print("\x1b[%sm  Backup complete... \x1b[0m" % colors['blue'])
