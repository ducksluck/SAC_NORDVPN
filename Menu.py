import os
from DownloadCountry import DownloadCountry
from DownloadAllDoubles import DownloadAllDoubles
from ShowDoubleVPN import ShowDoubleVPN
from ShowCountries import ShowCountries
from ConnectCountry import ConnectCountry
from ConnectRandom import ConnectRandom
from Kill_VPN_Proc import Kill_VPN_Proc
from RemoveOldConfigs import RemoveOldConfigs
from getLinks import getLinks
from ChangeColors import ChangeColors
from FColor import FColor
from BackupConfigs import BackupConfigs


def PrintMenu(colors):
    menu_items = []
    print("\n \x1b[%sm  Options: \x1b[0m \n" % colors['color_box1'])
    menu_items.append("\t \x1b[%sm [1] \x1b[0m \x1b[%sm Connect: Random NordVPN server \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [2] \x1b[0m \x1b[%sm Connect: Selected  Country \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [3] \x1b[0m \x1b[%sm Show/Connect: 'Double VPNs' \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [4] \x1b[0m \x1b[%sm Show Configs: (Downloaded Countries) \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [5] \x1b[0m \x1b[%sm Download: All Configs & Purge Old \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [6] \x1b[0m \x1b[%sm Download: Selected Country & Purge existing from country \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [7] \x1b[0m \x1b[%sm Download: Double VPNs \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [D] \x1b[0m \x1b[%sm [D]isconnect from VPN \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [Q] \x1b[0m \x1b[%sm [Q]uit RandoVPN & Stay Connected \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [C] \x1b[0m \x1b[%sm [C]hange Color \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    menu_items.append("\t \x1b[%sm [B] \x1b[0m \x1b[%sm [B]ackup Configs \x1b[0m" % (colors['color_box1'], colors['color_box2']))

    for option in menu_items:
        padding = (100 - len(option))*" "
        row = option[:-5]+padding+option[-5:]
        print(row)

    msg = " \x1b[%sm Select Option: \x1b[0m " % colors['color_box1']
    MenuNumber = input("\n"+msg)
    return MenuNumber


def Menu():
    configPoolDir = os.getcwd()+'\\ovpnConfigs\\'
    if not os.path.isdir(configPoolDir):
        os.mkdir(configPoolDir)

    # Create dict of colors
    colors = FColor('', '')
    prefPath = os.getcwd()+"\\colorpref.conf"   # path of color preference file is same dir as this script

    # Load color preferences if they exist.
    if os.path.isfile(prefPath):
        preferred_colors = []
        confFile = open(prefPath, "r")
        contents = confFile.read()
        lines = contents.split('\n')
        for x in lines:
            if x != '\n':
                preferred_colors.append(x.split(':')[1])
        confFile.close()

    # Menu Selection Logic
    SelectQuit = False
    while SelectQuit is False:                            # MAIN LOOP
        selection = PrintMenu(colors)                     # MENU
        if selection == '1':
            ConnectRandom(configPoolDir, colors)
        elif selection == '2':
            ConnectCountry(configPoolDir, colors)
        elif selection == '3':
            ShowDoubleVPN(configPoolDir, colors)
        elif selection == '4':
            ShowCountries(configPoolDir, colors)          # (excludes double VPNs)
        elif selection == '5':
            RemoveOldConfigs("All", configPoolDir, colors)
            getLinks("All", configPoolDir, colors)        # Download All Configs
        elif selection == '6':                            # Colors
            DownloadCountry(configPoolDir, colors)
        elif selection == '7':                            # Download Douple VPN
            DownloadAllDoubles(configPoolDir, colors)
        elif selection == 'C' or selection == 'c':        # Change colors
            colors = ChangeColors(colors, prefPath)
        elif selection == 'B' or selection == 'b':        # Change colors
            BackupConfigs(configPoolDir, colors)
        elif selection == 'D' or selection == 'd':        # Disconnect / Kill OpenVPN Processes
            Kill_VPN_Proc(1)
        elif selection == 'Q' or selection == 'q':        # Quit randomVPN NOT openVPN
            SelectQuit = True

        else:
            print("\x1b[%sm  Invalid Option: \x1b[0m" % colors['red_box'])
            import time
            time.sleep(1.5)


if __name__ == "__main__":
    Menu()
