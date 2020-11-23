import os


def RemoveOldConfigs(scope, configPoolDir, colors):
    # Delete All Old Configs
    if scope == "All":
        for filename in os.listdir(configPoolDir):
            path = os.path.join(configPoolDir, filename)
            try:
                if filename[-5:] == ".ovpn":
                    os.remove(path)
            except Exception as e:
                print('\x1b[%sm  Delete Failed %s. Error: %s \x1b[0m' % (colors['red_box'], path, e))

    # Delete Double VPNs
    elif "-" in scope:
        for filename in os.listdir(configPoolDir):
            path = os.path.join(configPoolDir, filename)
            try:
                if filename[-5:] == ".ovpn" and "-" in filename:
                    os.remove(path)
            except Exception as e:
                print('\x1b[%sm  Delete Failed %s. Error: %s \x1b[0m' % (colors['red_box'], path, e))

    # Delete Selected Country
    else:
        for filename in os.listdir(configPoolDir):
            path = os.path.join(configPoolDir, filename)
            try:
                if filename[-5:] == ".ovpn" and filename.startswith(scope):
                    os.remove(path)
            except Exception as e:
                print('\x1b[%sm  Delete Failed %s. Error: %s \x1b[0m' % (colors['red_box'], path, e))
