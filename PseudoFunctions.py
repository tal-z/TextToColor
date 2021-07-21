# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:56:33 2021

@author: tzaken
"""

import pandas as pd
import colorsys
from tkinter import Tk

colornames_df = pd.read_csv('colornames.txt', delimiter=" ", skiprows=60, header=None)
colornames_df.columns = ['IDX', 'NAME', 'rgb', 'R', 'G', 'B', 'hex', 'HEX', 'hsv', 'h', 's', 'v', 'xyz', 'X', 'Y', 'Z',
                         'lab', 'L', 'A', 'B', 'lch', 'L', 'C', 'H', 'cmyk', 'C', 'M', 'Y', 'K', 'NEIGHBOUR_STR',
                         'NUM_NEIGHBOURS_MAXDE', 'WORD_TAGS']


def words_to_colors(input=str):
    """
    Takes a string as input.    
    Tokenizes the string. 
    Looks for tokens that represent colors. --> converts tokens to hex codes
    Looks for tokens that modify color tokens. --> modifies hex code dependent on description.
    """


def look_up_color(token=str):
    """
    Takes a token, and checks whether it is present in a pre-defined dictionary of colors
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


def darken_color(hex_str=str, darkening_value=.5):
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


def lighten_color(hex_str=str, lightening_value=.5):
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
    Takes a properly-formattend hex color code as input, 
    and opens a window displaying the color. 
    """
    hex_str = hex_str.lstrip('#')
    gui = Tk(className=f'Hex Color Code #{hex_str}')
    gui.geometry("400x200")
    gui.configure(bg=f"#{hex_str}")
    gui.mainloop()


if __name__ == '__main__':
    sample_hex = look_up_color('negroni')
    show_color(sample_hex[0])
    show_color(lighten_color(sample_hex[0]))
    show_color(darken_color(sample_hex[0]))
    show_color(brighten_color(sample_hex[0]))
