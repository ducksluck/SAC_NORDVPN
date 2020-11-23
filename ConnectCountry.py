import os
import random
from ShowCountries import ShowCountries
from launchVPN import launchVPN


def ConnectCountry(configPoolDir, colors):

    select_msg = "\x1b[%sm    Enter country abbreviation: \x1b[0m " % colors['color2']
    selectedCountry = input(select_msg)

    # Select VPN config types
    print("\n \x1b[%sm Select VPN Connection type: \x1b[0m \n" % colors['color_box1'])
    print("\t \x1b[%sm [1] \x1b[0m \x1b[%sm TCP configs \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    print("\t \x1b[%sm [2] \x1b[0m \x1b[%sm UDP configs \x1b[0m" % (colors['color_box1'], colors['color_box2']))
    selectmsg = "\n \x1b[%sm Select Connection Type \x1b[0m " % colors['color_box1']
    tcp_udp = input(selectmsg)
    if tcp_udp == '1':
        tcp_udp = 'tcp443'
    elif tcp_udp == '2':
        tcp_udp = 'udp1194'


    available = []
    files = os.listdir(configPoolDir)
    found = False
    for c in files:
        if c[:len(selectedCountry)] == selectedCountry and c.__contains__(tcp_udp):
            available.append(c)
            found = True
    if found is False:
        print("\x1b[%sm  There are no VPN Servers available from that country. Try downloading country first\x1b[0m" % colors['red_box'])
        ShowCountries(configPoolDir, colors)

    else:
        randomSelect = available[random.randrange(0, len(available))]
        random_msg = "    Random " + selectedCountry.upper() + " Server: " + randomSelect
        print("\x1b[%sm %s \x1b[0m" % (colors['color2'], random_msg))
        launchVPN(randomSelect, configPoolDir, colors)
