
from tkinter import Tk, Text, INSERT

from show_color import show_named_color, show_coded_color
from conversions import *
from namelookup import *
from helpers import *

class ColorController:

    def __init__(self, hex_code=None, rgb=None, hsv=None, name=None):
        """Initialize class with one and only one of four optional attributes. If multiple attributes are passed,
        only one is used. The order of use is hex_code, rgb, hsv, name. You should only pass one of these arguments upon
        initializing a new ColorController object."""
        if hex_code:
            self._hex_code = hex_code
            self._rgb = hex_to_rgb(hex_code)
            r, g, b = self._rgb
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            self._hsv = (float('%.3g' % h), float('%.3g' % s), int('%.3g' % v))
            self._name = find_closest_color_names(hex_code)
        elif rgb:
            r, g, b = rgb
            self._hex_code = rgb_to_hex(r, g, b)
            self._rgb = rgb
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            self._hsv = (float('%.3g' % h), float('%.3g' % s), int('%.3g' % v))
            self._name = find_closest_color_names(self._hex_code)
        elif hsv:
            h, s, v = hsv
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            self._rgb = int(r), int(g), int(b)
            self._hex_code = rgb_to_hex(r, g, b)
            self._hsv = hsv
            self._name = find_closest_color_names(self._hex_code)
        elif name:
            self._hex_code = query_hex_code(name)
            self._rgb = [hex_to_rgb(code) for code in self._hex_code]
            hsv_list = []
            for color in self._rgb:
                r, g, b = color
                h, s, v = colorsys.rgb_to_hsv(r, g, b)
                hsv_list.append((float('%.3g' % h), float('%.3g' % s), int('%.3g' % v)))
            self._hsv = hsv_list
            self._name = name

    @property
    def name(self):
        """
        Because I want to auto-update values as they are called, I have selected to use "getters and setters,"
        implemented in Python as class properties. This is the "getter" method, and it's job is to return
        the .name property. It works by  checking to see if there is a name set in the ._name attribute,
        and returns the name if there is. Because name is always set upon init, the check is redundant.
        """
        if self._name:
            return self._name


    @name.setter
    def name(self, new_name):
        """
        The decorator here is fairly clear that this is the "setter" method for the name property. When an instance of
        a ColorController object is provided with a new name property, this bit of code is responsible for updating all
        of the other properties. This is where the magic happens.
        """
        self._name = new_name
        self._hex_code = query_hex_code(new_name)
        self._rgb = [hex_to_rgb(code) for code in self._hex_code]
        hsv_list = []
        for color in self._rgb:
            r, g, b = color
            hsv_list.append(colorsys.rgb_to_hsv(r, g, b))
        self._hsv = hsv_list

    @property
    def hex_code(self):
        """This is the hex_code getter.
        It works the same way as the name getter, but on hex_code."""
        if self._hex_code:
            return self._hex_code


    @hex_code.setter
    def hex_code(self, new_hex_code):
        """
        This is the hex_code setter. It also works the same as the name_setter.
        """
        self._hex_code = new_hex_code
        self._name = find_closest_color_names(new_hex_code)
        self._rgb = hex_to_rgb(new_hex_code)
        r, g, b = self._rgb
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def rgb(self):
        """This is the rgb getter."""
        if self._rgb:
            return self._rgb


    @rgb.setter
    def rgb(self, new_rgb):
        """This is the rgb setter."""
        self._rgb = new_rgb
        r, g, b = self._rgb
        self._name = find_closest_color_names(rgb_to_hex(r, g, b))
        self._hex_code = rgb_to_hex(r, g, b)
        self._hsv = colorsys.rgb_to_hsv(r, g, b)

    @property
    def hsv(self):
        """This is the hsv getter."""
        if self._hsv:
            return self._hsv


    @hsv.setter
    def hsv(self, new_hsv):
        """This is the hsv setter. It has one extra step, because it is necessary
        to unpack the .hsv 3-tuple in order to convert back to rgb.
        """
        self._hsv = new_hsv
        h, s, v = new_hsv
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(r), int(g), int(b)
        self._name = find_closest_color_names(rgb_to_hex(r, g, b))
        self._hex_code = rgb_to_hex(r, g, b)
        self._rgb = r, g, b


    def show_codedcolor(self):
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
        text.insert(INSERT, f' Hex Color Code: {self._hex_code}\n\n')
        text.insert(INSERT, f' RGB Triplet: {self.rgb}\n\n')
        text.insert(INSERT, f' HSV Triplet: {self.hsv}\n\n')
        text.insert(INSERT, f' Color Name(s): {self.name}\n')
        text.pack()
        gui.mainloop()

    def darken_color(self, darkening_value=.25):
        """
        Takes a hex code and returns a hex code for a darker shade of the original hex code.
        Takes "darkening_value" as an optional input. Darkening value is a float between 0 and 1.
        """
        print("darkening color")
        h, s, v = unlist(self.hsv)
        v = v * (1 - darkening_value)
        self.hsv = (float('%.3g' % h), float('%.3g' % s), int('%.3g' % v))

    def lighten_color(self, lightening_value=.25):
        """
        Takes a hex code and returns a hex code for a lighter shade of the original hex code.
        Takes "lightening_value" as an optional input. Lightening value is a float between 0 and 1.
        """
        print("lightening color")
        h, s, v = unlist(self.hsv)
        s = s * (1 - lightening_value)
        self.hsv = (float('%.3g' % h), float('%.3g' % s), int('%.3g' % v))

    def brighten_color(self, brightening_value=.25):
        """
        Takes a hex code and returns a hex code for a brighter shade of the original hex code.
        Takes "brightening_value" as an optional input. Brightening value is a float between 0 and 1.
        """
        print("brightening color")
        h, s, v = unlist(self.hsv)
        s = min((s + ((1 - s) * brightening_value)), 1)
        v = min((v * (1 + brightening_value), 255))
        self.hsv = (float('%.3g' % h), float('%.3g' % s), int('%.3g' % v))

    def show_color(self):
        if type(self.hex_code) == list:
            show_named_color(self)
        else:
            show_coded_color(self)




if __name__ == '__main__':
    name = "ab902e"#sorted(colors_df.NAME.tolist(), key=lambda x: len(x))[-320].replace("_", " ")
    color = ColorController(hex_code=name)
    color.show_color()
    color.lighten_color(1)
    color.show_color()
    color.darken_color(.2)
    color.show_color()
    color.brighten_color(1)
    color.show_color()
