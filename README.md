# ColorController.py

Welcome to the ColorController Python library! 

My name is Tal Zaken, and I wrote this library for use in a natural language processing project 
that aims to take in free-form text, and spit out color data which somehow relates to the text's 
content. 

Enough about that. Here are some things that you can do with ColorController:

### 1. Encode color data in various formats.
#### Example 1.1: Create a ColorController object using a familiar, english-language color name, and print out its properties.

You can set a color using a very large library of color names. 
See the colornames.txt document contained herein, with enormous thanks to 
[Martin Krzywinski](http://mkweb.bcgsc.ca/colornames). 

The following code:
```python
from ColorController import ColorController

color = ColorController(name='yellow')

print(f"Name: {color.name}", 
      f"Hex Code: {color.hex_code}", 
      f"RGB: {color.rgb}", 
      f"HSV: {color.hsv}", 
      sep='\n')
```
outputs:
```
Name: yellow
Hex Code: #FFFF14
RGB: (255, 255, 20)
HSV: (0.16666666666666666, 0.9215686274509803, 255)
```
Further, you can change all of the ColorController's properties by changing any one of them. 
By example:
```python
color.name = 'blue'

print(f"Name: {color.name}", 
      f"Hex Code: {color.hex_code}", 
      f"RGB: {color.rgb}", 
      f"HSV: {color.hsv}", 
      sep='\n')
```
You will see that all properties have updated:
```
Name: blue
Hex Code: ['#00008B', '#0000CD', '#0000EE', '#0000FF', '#0087BD', '#0093AF', '#0018A8', '#0247FE', '#0343DF', '#1F75FE', '#2242C7', '#333399']
RGB: (51, 51, 153)
HSV: (0.6666666666666666, 0.6666666666666666, 153)
```
Notably, the colornames.txt file has numerous entries that all share the name "blue." This is true of many colors.
Because color is thought to be a culturally relative phenomenon, I have chosen to return all hex codes that match a given name. 
You will notice a similar phenomenon occurs for color names when you set a color using hex code, RGB, or HSV. 
This is because there are sometimes many names that all describe the same color. 

That said, the ColorController object is biased toward whatever you, the user, set it to be. 
If you explicitly set a name, then that will be the singular name of your object.
Similarly, if you explicitly set a hex code, then that will be the value of your hex code. 
If you leave  a leading # off of your hex code, 
then everything will still work, but that will be the hex code value. For example...

#### Example 1.2: Create a ColorController object using a hex code, and print out its properties.
```python
c = ColorController(hex_code='#990000')

print(f"Name: {c.name}",
      f"Hex Code: {c.hex_code}",
      f"RGB: {c.rgb}",
      f"HSV: {c.hsv}",
      sep='\n')
```
Outputs:
```
Name: ['stizza', 'usc_cardinal', 'ou_crimson_red', 'crimson_red']
Hex Code: #990000
RGB: (153, 0, 0)
HSV: (0.0, 1.0, 153)
```
While:
```python
c = ColorController(hex_code='990000')

print(f"Name: {c.name}",
      f"Hex Code: {c.hex_code}",
      f"RGB: {c.rgb}",
      f"HSV: {c.hsv}",
      sep='\n')
```
Also outputs:
```
Name: ['stizza', 'usc_cardinal', 'ou_crimson_red', 'crimson_red']
Hex Code: 990000
RGB: (153, 0, 0)
HSV: (0.0, 1.0, 153)
```
#### Example 1.3: Create a ColorController object using an RGB triplet, and print out its properties.
```python
c = ColorController(rgb=(10, 255, 230))

print(f"Name: {c.name}",
      f"Hex Code: {c.hex_code}",
      f"RGB: {c.rgb}",
      f"HSV: {c.hsv}",
      sep='\n')
```
```
Name: ['bright_aqua']
Hex Code: #0affe6
RGB: (10, 255, 230)
HSV: (0.4829931972789116, 0.9607843137254902, 255)
```
#### Example 1.4: Create a ColorController object using an HSV triplet, and print out its properties.

### 2. Modify a color, and keep track of changes to the color in all available formats.
### 3. Show a color. 
### 4. Invert a color.


## Known Bugs:
  - Although I return multiple hex codes given a color name, 
    I'm only returning one rgb and hsv. 
    I should always have the same number of hex, rgb, and hsv values. 
    NOTE: Where there are discrepancies in the number of hex codes and rgb/hsv values, 
    the rgb and hsv always relate to the last list item.

## Resources:
  - What is color?: https://www.crayola.com/for-educators/resources-landing/articles/color-what-is-color.aspx
  - unofficial crayola colors: https://www.w3schools.com/colors/colors_crayola.asp
  - color names database: http://mkweb.bcgsc.ca/colornames/
  - interactive color code tool: https://www.hexcolortool.com/#3cec71
  - NLTK Information extraction chapter: http://www.nltk.org/book/ch07.html
  - colorsys source code: https://github.com/python/cpython/blob/3.9/Lib/colorsys.py
  - webcolors source code: https://github.com/ubernostrum/webcolors/blob/trunk/src/webcolors.py
    - Note: while I'm not using webcolors in this program, I'm looking at their hex conversion algorithms to better understand the concept and see how it gets implemented.
  - explanation of calculating distance in hsv space: https://stackoverflow.com/questions/35113979/calculate-distance-between-colors-in-hsv-space
