from ColorController import ColorController
from ColorController.helpers import regular_round



def mix_rgb(rgb1, rgb2):
    return tuple(int(regular_round(sum([ch1, ch2]) / 2)) for (ch1, ch2) in zip(rgb1, rgb2))


c1 = ColorController(hex_code='ff0000')

c1.show_color()
c2 = ColorController(hex_code='00ffff')

c2.show_color()
color = ColorController(rgb=mix_rgb(c1.rgb, c2.rgb))
color.show_color()
