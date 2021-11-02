from ColorController.conversions import invert_rgb
from ColorController import ColorController


color = ColorController(hex_code='#9ffeb0')
color.show_color()

r, g, b = color.rgb
color.rgb = invert_rgb(r, g, b)
color.show_color()
