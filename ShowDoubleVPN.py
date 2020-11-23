import os
import random
from launchVPN import launchVPN


def ShowDoubleVPN(configPoolDir, colors):
    doubleVPNs = []
    files = os.listdir(configPoolDir)
    for x in files:
        if x[2] == '-':
            prefixEndIndex = x.index(".")
            server = x[:prefixEndIndex]
            abbr = x[:5]
            if doubleVPNs == []:
                doubleVPNs.append([abbr, server])   # append new list with row header and server
            else:
                abbrevFound = False
                for record in doubleVPNs:
                    if record[0] == abbr:
                        if record.__contains__(server):   # dismiss duplicates
                            abbrevFound = True
                            pass
                        else:
                            doubleVPNs[doubleVPNs.index(record)].append(server)
                            abbrevFound = True
                            continue
                # new country found
                if abbrevFound is False:
                    doubleVPNs.append([abbr, server])  # append new list with row header and server

    print("\n\x1b[%sm  Available Double VPNs Countries and Servers: \x1b[0m" % colors['color1'])
    count = 0
    if not doubleVPNs:
        print("\x1b[%sm No double VPN configs downloaded! Do so via the main menu first. \x1b[0m" % colors['red_box'])
        return
    max_value = max(doubleVPNs)

    while count < len(doubleVPNs):
        row = doubleVPNs[count]
        # Padding left column
        if count < 9:
            row_num = "      " + str(count + 1) + " "
        else:
            row_num = "     " + str(count + 1) + " "

        row_num = row_num + row[0]
        max_string = str(max_value)
        print("\x1b[%sm %s \x1b[0m" % (colors['color_box1'], row_num), end="")
        country_row = str(row[1:])
        blue_padding = " "*(len(max_string) - len(country_row))
        server_column = country_row[1:-1] + blue_padding
        print("\x1b[%sm %s \x1b[0m" % (colors['color_box2'], server_column))

        count = count + 1

    msg = "\x1b[%sm   Select row # of desired Country Pair or '0' for none: \x1b[0m " % colors['color1']
    try:
        rowChoice = int(input("\n" + msg))
    except:   # Input not an int
        print("\x1b[%sm That is not a valid option. \x1b[0m" % colors['red_box'])
        return

    if rowChoice == 0:
        pass
    elif rowChoice-1 >= len(doubleVPNs):
        print("\x1b[%sm That is not a valid option. \x1b[0m" % colors['red_box'])
    else:
        doubleChoice = doubleVPNs[rowChoice-1]
        # print("Available Servers: ", doubleChoice)
        randomDouble = random.randrange(1, len(doubleChoice))
        selectedDouble = doubleChoice[randomDouble]
        print("\x1b[%sm  Random Selection: \x1b[0m \x1b[%sm %s \x1b[0m" % (colors['color1'], colors['color2'], selectedDouble))
        launchVPN(selectedDouble + ".nordvpn.com.tcp443.ovpn", configPoolDir, colors)


