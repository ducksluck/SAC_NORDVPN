import os


def ShowCountries(configPoolDir, colors):
    uniqueCountries = []
    configFiles = os.listdir(configPoolDir)

    # Make list of country abbreviations and double VPNs
    for x in configFiles:
        temp = ""
        # check each letter until a number is reached
        for i in x:
            if i.isalpha() or i == '-':
                temp = temp + i
            else:
                break
        if uniqueCountries.__contains__(temp):
            continue
        else:
            if temp.__contains__("-") is False:
                uniqueCountries.append(temp)

    if not uniqueCountries:
        msg = "\x1b[%smNo configs available. Download configs via the main menu.\x1b[0m" % colors['red']
        print(msg)

   # Print out table of downloaded configs by country
    else:
        msg = "\n  \x1b[%smAvailable Countries: \x1b[0m" % colors['color1']
        print(msg)

        count = 0
        lastcolor = colors['color_box1']
        currentcolor = colors['color_box2']
        print("     ", end='')   # padding for first row in table of countries
        for country in uniqueCountries:
            count += 1
            if count % 10 == 0:
                print("\x1b[%sm %s \x1b[0m\n     " % (currentcolor, country), end='')
            else:
                print("\x1b[%sm %s \x1b[0m" % (currentcolor, country), end="")

            # Rotate colors
            if lastcolor == colors['color_box2']:
                lastcolor = colors['color_box1']
                currentcolor = colors['color_box2']
            else:
                lastcolor = colors['color_box2']
                currentcolor = colors['color_box1']

        print("\n")

