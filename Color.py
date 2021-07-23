import colorsys
from math import sin, cos, pi

import pandas as pd

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
    token = token.replace(" ", "_")
    return list(colors_df.query(f'NAME=="{token.lower()}"').HEX)


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
            self._name = self.find_closest_color_name(self._hex_code)
            return self._name
        elif self._rgb:
            r, g, b = self._rgb
            self._name = self.find_closest_color_name(rgb_to_hex(r, g, b))
            return self._name
        elif self._hsv:
            h, s, v = self._hsv
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            self._name = self.find_closest_color_name(rgb_to_hex(r, g, b))
            return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self._hex_code = query_hex_code(new_name)
        self._rgb = hex_to_rgb(self._hex_code[-1])
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def hex_code(self):
        if self._hex_code:
            return self._hex_code
        elif self._name:
            self._hex_code = query_hex_code(self._name)
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

    @hex_code.setter
    def hex_code(self, new_hex_code):
        self._hex_code = new_hex_code
        self._name = self.find_closest_color_name(new_hex_code)
        self._rgb = hex_to_rgb(new_hex_code)
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    # PICK UP HERE: Need to write getters and setters for rgb and hsv
    @property
    def rgb(self):
        if self._rgb:
            return self._rgb
        elif self._name:
            self._rgb = hex_to_rgb(query_hex_code(self._name))
            return self._rgb
        elif self._hex_code:
            self._rgb = hex_to_rgb(self._hex_code)
            return self._rgb
        elif self._hsv:
            h, s, v = self._hsv
            self._rgb = colorsys.hsv_to_rgb(h, s, v)
            return self._rgb

    @rgb.setter
    def rgb(self, new_rgb):
        self._rgb = new_rgb
        self._name = self.find_closest_color_name(rgb_to_hex(new_rgb))
        self._hex_code = rgb_to_hex(new_rgb)
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def hsv(self):
        if self._hsv:
            return self._hsv
        elif self._name:
            r, g, b = hex_to_rgb(query_hex_code(self._name[-1])[-1])
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv
        elif self._hex_code:
            r, g, b = hex_to_rgb(self._hex_code)
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv
        elif self._rgb:
            r, g, b = self._rgb
            self._hsv = colorsys.rgb_to_hsv(r, g, b)
            return self._hsv

    @hsv.setter
    def hsv(self, new_hsv):
        self._hsv = new_hsv
        h, s, v = new_hsv
        self._name = self.find_closest_color_name(rgb_to_hex(colorsys.hsv_to_rgb(h, s, v)))
        self._hex_code = rgb_to_hex(colorsys.hsv_to_rgb(h, s, v))
        self._rgb = colorsys.hsv_to_rgb(h, s, v)

    def find_closest_color_name(self, hex_str=str):
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


a = ColorController(rgb=(10, 30, 100))
print(a.hsv, a.name)

