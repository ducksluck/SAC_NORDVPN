import os
from Kill_VPN_Proc import Kill_VPN_Proc


def kill_logic(colors):
    killedP = Kill_VPN_Proc()
    if killedP is True:    # Double check killed process actually terminated
        Kill_VPN_Proc()
        import time
        print("\x1b[%sm Waiting for old process to completely close.\x1b[0m" % colors['color2'])
        time.sleep(4)


def launchVPN(server, configPoolDir, colors):
    print("\x1b[%sm  Checking for running OpenVPN Processes... \x1b[0m" % colors['color1'])
    kill_logic(colors)

    from shutil import copyfile
    srcFile = configPoolDir + server
    dest = "C:\\Program Files\\OpenVPN\\config\\"
    destFile = dest + server

    # Before you look at the next statements and your mind explodes:
    #
    # WTF WHY?!?!?!
    # (ノ°Д°）ノ︵ ┻━┻
    #
    # you looked...(i know you did)
    # ok well I write the file config to the default openvpn config directly just so it can be deleted.
    # yes there it is in all it's glory.
    #
    # If openvpn was connected prior to running this script, the OpenVPN processes would be killed (as intended),
    # The subprocess.popen command below launches OpenVPN to the taskbar.
    # However, it wouldn't attempt to establish a connection and open the login gui.
    #
    # I noticed it would however if the config was already in the dir
    # and the if the statement is executed to remove it.
    # (Note: it doesn't matter if the current config being loaded is the one that was used before
    #   or a new config that's never been used)
    #
    # Any suggestions?

    try:
        copyfile(srcFile, destFile)
    except:
        pass
    if os.path.isfile(destFile.strip()):
        os.remove(destFile)
    copyfile(srcFile, destFile)

    # Launch OpenVPN
    connect_cmd = '"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --connect ' + server

    # Run OpenVPN as subprocess which will keep running when script is properly exited via the menu
    import subprocess
    subprocess.Popen(connect_cmd, shell=True, close_fds=True)
