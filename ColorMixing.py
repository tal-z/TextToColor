from ColorController import ColorController
from ColorController.helpers import regular_round



def mix_rgb(rgb1, rgb2):
    return tuple(int(regular_round(sum([ch1, ch2]) / 2)) for (ch1, ch2) in zip(rgb1, rgb2))


c1 = ColorController(name='maroon')
c1.show_color()
for i in range(10):
    c1.hex_code = str(int('193123') + 1000*i)
    c1.show_color()
