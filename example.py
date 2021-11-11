from ColorController.conversions import invert_rgb
from ColorController import ColorController
import matplotlib.pyplot as plt

grey = ColorController(name='green')
grey.show_color()

red = ColorController(hex_code='#ff0000')
red.show_color()

red.lighten_color()
red.show_color()

grey = ColorController(name='grey')
grey.show_color()