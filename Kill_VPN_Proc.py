import os


# kill any running openvpn services
def Kill_VPN_Proc():
    tasklist = os.popen('tasklist').readlines()
    killed = False
    for task in tasklist:
        try:
            if "openvpn-gui.exe" in task:
                os.system("Start /WAIT taskkill /F /im openvpn-gui.exe")
                killed = True
        except:
            continue
        try:
            if "openvpnserv.exe" in task:
                os.system("Start /WAIT taskkill /F /im openvpnserv.exe")
                killed = True
        except:
            continue
        try:
            if "openvpn.exe" in task:
                os.system("Start /WAIT taskkill /F /im openvpn.exe")
                killed = True
        except:
            continue

    return killed

