#from ColorController import ColorController, colors_df
import matplotlib.pyplot as plt
from conversions import invert_rgb, rgb_to_hex


def place_title_linebreak(title):
    title = title.split(" ")
    new_title = ""
    line = ""
    for word in title:
        if len(line) + len(word) <= 17:
            line += word + " "
            new_title += word + " "
        else:
            new_title += word + "\n"
            line = ""
    return new_title


def set_title_fontsize(title):
    fontsize=40
    title_len = len(title)
    if title_len > 15:
        fontsize = 50-title_len
    return fontsize


def show_named_color(color_object):
    data = [1 for code in color_object.hex_code]
    explode = [.05 for d in data]
    plt.pie(data, explode=explode, labels=color_object.hex_code, colors=color_object.hex_code)
    plt.title(place_title_linebreak(color_object.name.upper()), fontsize=set_title_fontsize(color_object.name))
    plt.tight_layout()
    plt.show()


def show_coded_color(color_object):
    data = [1 for name in color_object.name]
    hex_str = "#" + color_object.hex_code.lstrip('#')
    plt.pie(data, labels=color_object.name, colors=[hex_str for name in color_object.name], wedgeprops={'linewidth': .5, 'ec': hex_str})
    r, g, b = color_object.rgb
    text_r, text_g, text_b = invert_rgb(r, g, b)
    text_color = rgb_to_hex(text_r, text_g, text_b)
    plt.text(x=-.65, y=-.15, s=f'Hex Code: {color_object.hex_code}\n'
                             f'RGB: {color_object.rgb}\n'
                             f'HSV: {color_object.hsv}', color=text_color)
    #plt.title(place_title_linebreak(color_object.name.upper()), fontsize=set_title_fontsize(color_object.name))
    plt.show()

