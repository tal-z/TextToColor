# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:56:33 2021

@author: tzaken
"""

import pandas as pd
import colorsys
from tkinter import Tk
from nltk.tokenize import word_tokenize
import random
from math import sin, cos, pi

colornames_df = pd.read_csv('colornames.txt', delimiter=" ", skiprows=60, header=None)
colornames_df.columns = ['IDX', 'NAME', 'rgb', 'R', 'G', 'B', 'hex', 'HEX', 'hsv', 'h', 's', 'v', 'xyz', 'X', 'Y', 'Z',
                         'lab', 'L', 'A', 'B', 'lch', 'L', 'C', 'H', 'cmyk', 'C', 'M', 'Y', 'K', 'NEIGHBOUR_STR',
                         'NUM_NEIGHBOURS_MAXDE', 'WORD_TAGS']
colornames_df['WORD_TAGS'] = colornames_df['WORD_TAGS'].apply(lambda x: x.split(":"))


def words_to_color(text_input=str):
    """
    Takes a string as input.
    Tokenizes the string.
    Does some other unhelpful stuff.
    """
    words = word_tokenize(text_input)
    similarity_df = pd.DataFrame(colornames_df)
    similarity_df['similarity'] = similarity_df['WORD_TAGS'].apply(
        lambda x: len(set(words) & set(x)) / float(len(set(words) | set(x))) * 100)
    return (similarity_df.sort_values(by='similarity').iloc[-1].NAME,
            similarity_df.sort_values(by='similarity').iloc[-1].WORD_TAGS,
            similarity_df.sort_values(by='similarity').iloc[-1].similarity)


def look_up_color(token=str):
    """
    Takes a token, and checks whether it is present in a pre-defined dictionary of color names.
    If the token is found, it returns the full range of hex codes that match the color name.
    """
    token = token.replace(" ", "_")
    return list(colornames_df.query(f'NAME=="{token.lower()}"').HEX)


def color_to_hex(token=str):
    """
    takes a single-token string and returns a hex code.
    """


def hex_to_rgb(hex_str=str):
    """
    Return (red, green, blue) for the color given as #rrggbb.
    """
    hex_str = hex_str.lstrip('#')
    len_hex = len(hex_str)
    return tuple(int(hex_str[i:i + len_hex // 3], 16) for i in range(0, len_hex, len_hex // 3))


def rgb_to_hex(red, green, blue):
    """
    Return color as #rrggbb for the given color values.
    """
    return '#%02x%02x%02x' % (int(round(red)), int(round(green)), int(round(blue)))


def darken_color(hex_str=str, darkening_value=.25):
    """
    Takes a hex code and returns a hex code for a darker shade of the original hex code.
    Takes "darkening_value" as an optional input. Darkening value is a float between 0 and 1.
    """
    r, g, b = hex_to_rgb(hex_str)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    v = v * (1 - darkening_value)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    darker_hex = rgb_to_hex(r, g, b)
    return darker_hex


def lighten_color(hex_str=str, lightening_value=.25):
    """
    Takes a hex code and returns a hex code for a lighter shade of the original hex code.
    Takes "lightening_value" as an optional input. Lightening value is a float between 0 and 1.
    """
    r, g, b = hex_to_rgb(hex_str)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    s = s * (1 - lightening_value)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    darker_hex = rgb_to_hex(r, g, b)
    return darker_hex


def brighten_color(hex_str=str, brightening_value=.5):
    """
    Takes a hex code and returns a hex code for a brighter shade of the original hex code.
    Takes "brightening_value" as an optional input. Brightening value is a float between 0 and 1.
    """
    r, g, b = hex_to_rgb(hex_str)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    s = s + ((1 - s) * brightening_value)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    brighter_hex = rgb_to_hex(r, g, b)
    return brighter_hex


def show_color(hex_str=str):
    """
    Takes a properly-formatted hex color code as input,
    and opens a window displaying the color. 
    """
    hex_str = hex_str.lstrip('#')
    gui = Tk(className=f'Hex Color Code #{hex_str}')
    gui.geometry("400x200")
    gui.configure(bg=f"#{hex_str}")
    gui.mainloop()


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


if __name__ == '__main__':
    """
    sample_hex = random.choice(look_up_color('parsley'))
    show_color(sample_hex)
    show_color(lighten_color(sample_hex))
    show_color(darken_color(sample_hex))
    show_color(brighten_color(sample_hex))
    """
    color_name1 = 'blood red'
    color_name2 = 'deep red'
    show_color(look_up_color(color_name1)[-1])
    show_color(look_up_color(color_name2)[-1])
    rgb1 = hex_to_rgb(look_up_color(color_name1)[-1])
    rgb2 = hex_to_rgb(look_up_color(color_name2)[-1])
    hsv1 = colorsys.rgb_to_hsv(rgb1[0], rgb1[1], rgb1[2])
    hsv2 = colorsys.rgb_to_hsv(rgb2[0], rgb2[1], rgb2[2])
    hsv1 = colorsys_hsv_to_hsv360(hsv1)
    hsv2 = colorsys_hsv_to_hsv360(hsv2)
    hsv1 = hsv360_to_hsvdistance(hsv1)
    hsv2 = hsv360_to_hsvdistance(hsv2)

    print(hsv1, hsv2)
    print(measure_hsv_distance(hsv1, hsv2))
