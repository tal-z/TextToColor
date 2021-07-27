import colorsys
from math import sin, cos, pi

import pandas as pd
from tkinter import Tk, Text, INSERT, END

colors_df = pd.read_csv('colornames.txt', delimiter=" ", skiprows=60, header=None)
colors_df.columns = ['IDX', 'NAME',
                     'rgb', 'R', 'G', 'B',
                     'hex', 'HEX',
                     'hsv', 'h', 's', 'v',
                     'xyz', 'X', 'Y', 'Z',
                     'lab', 'L', 'A', 'B',
                     'lch', 'L', 'C', 'H',
                     'cmyk', 'C', 'M', 'Y', 'K',
                     'NEIGHBOUR_STR', 'NUM_NEIGHBOURS_MAXDE', 'WORD_TAGS']
colors_df['WORD_TAGS'] = colors_df['WORD_TAGS'].apply(lambda x: x.split(":"))


def invert_rgb(r, g, b):
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r, g, b


def unlist(data):
    if data == []:
        return ''
    elif type(data) == list:
        return data[-1]
    else:
        return data


def rgb_to_hex(red, green, blue):
    """
    Return color as #rrggbb for the given color values.
    """
    return '#%02x%02x%02x' % (int(round(red)), int(round(green)), int(round(blue)))


def hex_to_rgb(hex_str=str):
    """
    Return (red, green, blue) for the color given as #rrggbb.
    """
    hex_str = hex_str.lstrip('#')
    len_hex = len(hex_str)
    return tuple(int(hex_str[i:i + len_hex // 3], 16) for i in range(0, len_hex, len_hex // 3))


def colorsys_hsv_to_hsv360(colorsys_hsv=tuple):
    """
    Takes an HSV triplet as provided by colorsys, and converts it to match the
    notation used in colornames.txt
    """
    h = colorsys_hsv[0] * 360
    s = colorsys_hsv[1] * 100
    v = (colorsys_hsv[2] / 255) * 100
    corrected_hsv = (h, s, v)
    return corrected_hsv


def hsv360_to_hsvdistance(hsv360=tuple):
    """
    Takes an HSV triplet as provided by colorsys, and converts it to match the
    notation used in colornames.txt
    """
    h = (hsv360[0] / 360) * (2 * pi)
    s = hsv360[1] / 100
    v = hsv360[2] / 100
    corrected_hsv = (h, s, v)
    return corrected_hsv


def measure_hsv_distance(hsv1=tuple, hsv2=tuple):
    """
    Read this: https://stackoverflow.com/questions/35113979/calculate-distance-between-colors-in-hsv-space
    """
    h1, s1, v1 = hsv1
    h2, s2, v2 = hsv2
    distance = ((sin(h1) * s1 * v1 - sin(h2) * s2 * v2) ** 2
                + (cos(h1) * s1 * v1 - cos(h2) * s2 * v2) ** 2
                + (v1 - v2) ** 2)
    return distance


def query_hex_code(token=str):
    """
    Takes a token, and checks whether it is present in a pre-defined dictionary of color names.
    If the token is found, it returns the full range of hex codes that match the color name.
    """
    token = token.replace(" ", "_").lower()
    if token in colors_df.NAME.values:
        return list(colors_df.query(f'NAME=="{token.lower()}"').HEX)
    else:
        raise KeyError("Color name not found in colornames.txt")


def find_closest_color_name(hex_str=str):
    """Calculates distance between a given color hex code and every color in the colornames.txt database,
    and returns the a list of the closest color names.
    Only returns multiple results if there is a tie for the closest color.
    """
    r, g, b = hex_to_rgb(hex_str)
    h1, s1, v1 = colorsys.rgb_to_hsv(r, g, b)
    h1, s1, v1 = colorsys_hsv_to_hsv360((h1, s1, v1))
    h1, s1, v1 = hsv360_to_hsvdistance((h1, s1, v1))

    closenames_df = pd.DataFrame(colors_df)
    closenames_df['hsv'] = [(h, s, v) for h, s, v in
                            zip(closenames_df['h'], closenames_df['s'], closenames_df['v'])]
    closenames_df['hsv'] = closenames_df['hsv'].apply(hsv360_to_hsvdistance)
    closenames_df['distance'] = closenames_df['hsv'].apply(lambda x: measure_hsv_distance((h1, s1, v1), x))

    closest_distance = closenames_df.sort_values(by='distance').iloc[0].distance

    return list(set(closenames_df[closenames_df['distance'] == closest_distance].NAME))


class ColorController:

    def __init__(self, name=None, hex_code=None, rgb=None, hsv=None):
        self._name = name
        self._hex_code = hex_code
        self._rgb = rgb
        self._hsv = hsv

    @property
    def name(self):
        if self._name:
            return self._name
        elif self._hex_code:
            self._name = find_closest_color_name(self._hex_code)
            return self._name
        elif self._rgb:
            r, g, b = self._rgb
            hex_code = rgb_to_hex(r, g, b)
            self._name = find_closest_color_name(hex_code)
            return self._name
        elif self._hsv:
            h, s, v = self._hsv
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            self._name = find_closest_color_name(rgb_to_hex(r, g, b))
            return self._name

    @name.setter
    def name(self, new_name):
        print("name setter")
        self._name = new_name
        self._hex_code = query_hex_code(new_name)
        self._rgb = hex_to_rgb(self._hex_code[-1])
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def hex_code(self):
        if self._hex_code:
            return self._hex_code
        elif self._rgb:
            r, g, b = self._rgb
            self._hex_code = rgb_to_hex(r, g, b)
            return self._hex_code
        elif self._hsv:
            h, s, v = self._hsv
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            self._hex_code = rgb_to_hex(r, g, b)
            return self._hex_code
        elif self._name:
            self._hex_code = query_hex_code(self._name)[-1]
            return self._hex_code

    @hex_code.setter
    def hex_code(self, new_hex_code):
        self._hex_code = new_hex_code
        self._name = find_closest_color_name(new_hex_code)
        self._rgb = hex_to_rgb(new_hex_code)
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def rgb(self):
        if self._rgb:
            return self._rgb
        elif self._hex_code:
            self._rgb = hex_to_rgb(self._hex_code)
            return self._rgb
        elif self._hsv:
            h, s, v = self._hsv
            self._rgb = colorsys.hsv_to_rgb(h, s, v)
            return self._rgb
        elif self._name:
            self._rgb = hex_to_rgb(unlist(query_hex_code(unlist(self._name))))
            return self._rgb

    @rgb.setter
    def rgb(self, new_rgb):
        self._rgb = new_rgb
        r, g, b = self._rgb
        self._name = find_closest_color_name(rgb_to_hex(r, g, b))
        self._hex_code = rgb_to_hex(r, g, b)
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def hsv(self):
        if self._hsv:
            return self._hsv
        elif self._hex_code:
            r, g, b = hex_to_rgb(self._hex_code)
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv
        elif self._rgb:
            r, g, b = self._rgb
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv
        elif self._name:
            r, g, b = hex_to_rgb(unlist(query_hex_code(unlist(self._name))))
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv

    @hsv.setter
    def hsv(self, new_hsv):
        self._hsv = new_hsv
        h, s, v = new_hsv
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        self._name = find_closest_color_name(rgb_to_hex(r, g, b))
        self._hex_code = rgb_to_hex(r, g, b)
        self._rgb = colorsys.hsv_to_rgb(h, s, v)

    def show_color(self):
        """
        Takes a properly-formatted hex color code as input,
        and opens a window displaying the color.
        """

        hc = '#' + unlist(self.hex_code).lstrip('#')
        r_text, g_text, b_text = hex_to_rgb(hc)
        r_text, g_text, b_text = invert_rgb(r_text, g_text, b_text)
        text_color = rgb_to_hex(r_text, g_text, b_text)
        gui = Tk(className=f' Hex Color Code: {unlist(hc)}; Color Name: {unlist(self.name)} ')
        text = Text(gui, bg=f"{hc}", fg=text_color)
        text.insert(INSERT, f' Hex Color Code: {hc}\n')
        text.insert(INSERT, f' Color Name(s): {self.name}\n')
        text.insert(INSERT, f' RGB Triplet: {self.rgb}\n')
        text.insert(INSERT, f' HSV Triplet: {self.hsv}')

        text.pack()
        gui.geometry("400x200")
        gui.mainloop()

    def darken_color(self, darkening_value=.25):
        """
        Takes a hex code and returns a hex code for a darker shade of the original hex code.
        Takes "darkening_value" as an optional input. Darkening value is a float between 0 and 1.
        """
        print("darkening color")
        h, s, v = self.hsv
        v = v * (1 - darkening_value)
        self.hsv = (h, s, v)

    def lighten_color(self, lightening_value=.25):
        """
        Takes a hex code and returns a hex code for a lighter shade of the original hex code.
        Takes "lightening_value" as an optional input. Lightening value is a float between 0 and 1.
        """
        print("lightening color")
        h, s, v = self.hsv
        s = s * (1 - lightening_value)
        self.hsv = (h, s, v)

    def brighten_color(self, brightening_value=.25):
        """
        Takes a hex code and returns a hex code for a brighter shade of the original hex code.
        Takes "brightening_value" as an optional input. Brightening value is a float between 0 and 1.
        """
        print("brightening color")
        h, s, v = self.hsv
        s = min((s + ((1 - s) * brightening_value)), 1)
        v = min((v * (1 + brightening_value), 255))
        self.hsv = (h, s, v)


a = ColorController(name='yellow')
a.show_color()
a.lighten_color()
a.show_color()
a.brighten_color(1)
a.show_color()
