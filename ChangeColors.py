import os


def ChangeColors(colors, confPath):
    menu_items = []
    print("\n \x1b[%sm  Color Options: \x1b[0m" % colors['white_box'])
    menu_items.append("\t \x1b[%sm [1] \x1b[0m \x1b[%sm White \x1b[0m" % (colors['white_box'], colors['white']))
    menu_items.append("\t \x1b[%sm [2] \x1b[0m \x1b[%sm Connect: Selected  Country \x1b[0m" % (colors['red_box'], colors['red']))
    menu_items.append("\t \x1b[%sm [3] \x1b[0m \x1b[%sm Show/Connect: 'Double VPNs' \x1b[0m" % (colors['yellow_box'], colors['yellow']))
    menu_items.append("\t \x1b[%sm [4] \x1b[0m \x1b[%sm Show: Available Countries (except double VPNs) \x1b[0m" % (colors['orange_box'], colors['orange']))
    menu_items.append("\t \x1b[%sm [5] \x1b[0m \x1b[%sm Download: All Configs & Purge Old \x1b[0m" % (colors['blue_box'], colors['blue']))
    menu_items.append("\t \x1b[%sm [6] \x1b[0m \x1b[%sm Download: Selected Country & Purge existing from country \x1b[0m" % (colors['purple_box'], colors['purple']))
    menu_items.append("\t \x1b[%sm [7] \x1b[0m \x1b[%sm Download: Double VPNs \x1b[0m" % (colors['teal_box'], colors['teal']))

    for option in menu_items:
        padding = (100 - len(option))*" "
        row = option[:-5]+padding+option[-5:]
        print(row)

    first = int(input("Select Primary Color: "))
    second = int(input("Select Complimentary Color: "))

    if first == 1:
        colors['color_box1'] = colors['white_box']
        colors['color1'] = colors['white']
    elif first == 2:
        colors['color_box1'] = colors['red_box']
        colors['color1'] = colors['red']
    elif first == 3:
        colors['color_box1'] = colors['yellow_box']
        colors['color1'] = colors['yellow']
    elif first == 4:
        colors['color_box1'] = colors['orange_box']
        colors['color1'] = colors['orange']
    elif first == 5:
        colors['color_box1'] = colors['blue_box']
        colors['color1'] = colors['blue']
    elif first == 6:
        colors['color_box1'] = colors['purple_box']
        colors['color1'] = colors['purple']
    elif first == 7:
        colors['color_box1'] = colors['teal_box']
        colors['color1'] = colors['teal']

    # Set second color
    if second == 1:
        colors['color_box2'] = colors['white_box']
        colors['color2'] = colors['white']
    elif second == 2:
        colors['color_box2'] = colors['red_box']
        colors['color2'] = colors['red']
    elif second == 3:
        colors['color_box2'] = colors['yellow_box']
        colors['color2'] = colors['yellow']
    elif second == 4:
        colors['color_box2'] = colors['orange_box']
        colors['color2'] = colors['orange']
    elif second == 5:
        colors['color_box2'] = colors['blue_box']
        colors['color2'] = colors['blue']
    elif second == 6:
        colors['color_box2'] = colors['purple_box']
        colors['color2'] = colors['purple']
    elif second == 7:
        colors['color_box2'] = colors['teal_box']
        colors['color2'] = colors['teal']

    fileexists = os.path.isfile(confPath)
    if not fileexists:
        file = open(confPath, "w")
        preferences = 'color1:%s\ncolor2:%s\ncolor_box1:%s\ncolor_box2:%s' % (colors['color1'], colors['color2'], colors['color_box1'], colors['color_box2'])
        file.write(preferences)
        file.close()

    return colors



