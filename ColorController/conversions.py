from math import pi
import warnings


def invert_rgb(r, g, b):
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r, g, b


def rgb_to_hex(red, green, blue):
    """
    Return color as #rrggbb for the given color values. Does not handle unbounded values (bigger than 255).
    """
    if red > 255 or red < 0:
        raise ValueError("Inputs for red, green, and blue must be integer values between 0 and 255.")
    if green > 255 or green < 0:
        raise ValueError("Inputs for red, green, and blue must be integer values between 0 and 255.")
    if blue > 255 or blue < 0:
        raise ValueError("Inputs for red, green, and blue must be integer values between 0 and 255.")
    if type(red) != int:
        warnings.warn(f"Inputs for red, green, and blue must be integer values between 0 and 255. You entered type: {type(red)} for red.")
    if type(green) != int:
        warnings.warn(f"Inputs for red, green, and blue must be integer values between 0 and 255. You entered type: {type(green)} for green.")
    if type(blue) != int:
        warnings.warn(f"Inputs for red, green, and blue must be integer values between 0 and 255. You entered type: {type(blue)} for blue.")
    return '#%02x%02x%02x' % (int(round(red)), int(round(green)), int(round(blue)))


def hex_to_rgb(hex_str=str):
    """
    Return (red, green, blue) for the color given as #rrggbb. Values are integers only, as they should be.
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
    Takes an HSV triplet as provided by colorsys_hsv_to_hsv360(), and converts it to match the
    notation used in the function for calculating distance between colors.
    """
    h = (hsv360[0] / 360) * (2 * pi)
    s = hsv360[1] / 100
    v = hsv360[2] / 100
    corrected_hsv = (h, s, v)
    return corrected_hsv

