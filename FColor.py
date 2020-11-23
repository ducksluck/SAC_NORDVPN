

def FColor(primary, secondary):
    # Create dict of colors
    colors = {
        'white_box': '49;52;30',
        'red_box': '49;52;31',
        'yellow_box': '49;52;32',
        'orange_box': '49;52;33',
        'blue_box': '49;52;34',
        'purple_box': '49;52;35',
        'teal_box': '49;52;36',

        'white': "1;50;30",
        'red': "1;50;31",
        'yellow': "1;50;32",
        'orange': "1;50;33",
        'blue': '1;50;34',
        'purple': "1;50;35",
        'teal': "1;50;36",

        'color1': "1;50;32",
        'color2': '1;50;34',
        'color_box1': '49;52;32',
        'color_box2': '49;52;34',
    }

    if primary and secondary != '':
        colors['color1'] = "1;50;32"
        colors['color2'] = '1;50;34'
        colors['color_box1'] = '49;52;32'
        colors['color_box2'] = '49;52;34'

    return colors
