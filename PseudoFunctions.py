# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:56:33 2021

@author: tzaken
"""

import pandas as pd
from tkinter import *


with open('colornames.txt', 'r') as f:
    read_data = f.read()
    print(read_data)

df = pd.read_csv('colornames.txt', delimiter = " ", skiprows=60)



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
    

def show_color(hex_code=str):
    """
    Takes a properly-formattend hex color code as input, 
    and opens a window displaying the color. 
    """
    gui = Tk(className=f'Hex Color Code {hex}')
    gui.geometry("400x200")
    gui.configure(bg=hex)
    gui.mainloop() 
    

def color_to_hex(token=str):
    """takes a single-token string and returns a hex code."""    


def darken_color(hex_code=str, darkening_value=.5):
    """
    Takes a hex code and returns a hex code for a darker shade of the original hex code.
    Takes "darkening_value" as an optional input. Darkening value is a float between 0 and 1.
    """

    
def lighten_color(hex_code=str, lightness_value=.5):
    """
    Takes a hex code and returns a hex code for a lighter shade of the original hex code.
    Takes "lightening_value" as an optional input. Lightening value is a float between 0 and 1.
    """
    


    

show_color('#00002c')
