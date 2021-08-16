#from ColorController import ColorController, colors_df
import matplotlib.pyplot as plt


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


def show_namedcolor(color_object):
    data = [1 for code in color_object.hex_code]
    explode = [.05 for d in data]
    plt.pie(data, explode=explode, labels=color_object.hex_code, colors=color_object.hex_code)
    plt.title(place_title_linebreak(color_object.name.upper()), fontsize=set_title_fontsize(color_object.name))
    plt.tight_layout()
    plt.show()

