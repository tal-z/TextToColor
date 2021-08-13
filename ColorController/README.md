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
from ColorController.ColorController import ColorController

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

#### Example 1.2: Show a color.
We've had a lot of talk about colors so far, but we haven't even seen any colors yet! Let's solve that now, and enough of these lengthy print statements:
```python
color.hex_code ='#104bca'

color.show_color()
```
Shows:

![absolute_zero](https://github.com/tal-z/TextToColor/blob/main/ColorController/readmepics/absolute_zero.PNG?raw=true "absolute_zero.PNG")

That said, the ColorController object is biased toward whatever you, the user, set it to be. 
If you explicitly set a name, then that will be the singular name of your object.
Similarly, if you explicitly set a hex code, then that will be the value of your hex code. 
If you leave  a leading # off of your hex code, 
then everything will still work, but that will be the hex code value. For example...

#### Example 1.3: Create a ColorController object using a hex code.
```python
color = ColorController(hex_code='#990000')

color.show_color()
```
Shows:


![['crimson_red', 'stizza', 'ou_crimson_red', 'usc_cardinal']](https://github.com/tal-z/TextToColor/blob/main/ColorController/readmepics/crimson_red.PNG?raw=true "['crimson_red', 'stizza', 'ou_crimson_red', 'usc_cardinal']")


While:
```python
color = ColorController(hex_code='990000')

print(f"Name: {color.name}",
      f"Hex Code: {color.hex_code}",
      f"RGB: {color.rgb}",
      f"HSV: {color.hsv}",
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
You can also pass a 3-tuple whose values are each contained in range(0,256) to the rgb property. For example:
```python
color = ColorController(rgb=(10, 255, 230))

print(f"Name: {color.name}",
      f"Hex Code: {color.hex_code}",
      f"RGB: {color.rgb}",
      f"HSV: {color.hsv}",
      sep='\n')
```
Outputs:
```
Name: ['bright_aqua']
Hex Code: #0affe6
RGB: (10, 255, 230)
HSV: (0.4829931972789116, 0.9607843137254902, 255)
```
#### Example 1.4: Create a ColorController object using an HSV triplet, and print out its properties.
Lastly, you can also pass a 3-tuple whose first two values are a floating point number between 0 and 1 inclusive, and whose third value falls in range(0, 256):
```python
color = ColorController(hsv=(0.25, 1, 255))

print(f"Name: {color.name}",
      f"Hex Code: {color.hex_code}",
      f"RGB: {color.rgb}",
      f"HSV: {color.hsv}",
      sep='\n')
```
Outputs:
```
Name: ['luminous_vivid_chartreuse_green', 'medium_spring_green', 'chartreuse']
Hex Code: #80ff00
RGB: (128, 255, 0)
HSV: (0.25, 1, 255)
```

NOTE: While this is the HSV value format that comes included with the colorsys python standard library, it doesn't seem to be a very common format elsewhere. 
To match formats used in other locations, see the following functions:
```python
def colorsys_hsv_to_hsv360(colorsys_hsv=tuple):
    """Takes an HSV triplet as provided by colorsys, and converts it to match the
    notation used in colornames.txt"""

def hsv360_to_hsvdistance(hsv360=tuple):
    """Takes an HSV triplet as provided by colorsys_hsv_to_hsv360(), and converts it to match the
    notation used in the function for calculating distance between colors."""  
```
### 2. Modify a color using simple, convenient methods.
### 3. Show a color. 
### 4. Invert a color.
### 5. Access a rich set of color values and color names (prepared by Martin Krzywinski), conveniently stored in a Pandas DataFrame.
Example:

```python
from ColorController.ColorController import colors_df

print(colors_df.iloc[5000])
```
Outputs:
```
IDX                                                                  5000
NAME                                                    light_apple_green
rgb                                                                   rgb
R                                                                     220
G                                                                     231
B                                                                     139
hex                                                                   hex
HEX                                                               #DCE78B
hsv                                                                   hsv
h                                                                      67
s                                                                      40
v                                                                      91
xyz                                                                   xyz
X                                                                    0.63
Y                                                                    0.74
Z                                                                    0.35
lab                                                                   lab
L                                                                      89
A                                                                     -17
B                                                                      44
lch                                                                   lch
L                                                                      89
C                                                                      47
H                                                                     112
cmyk                                                                 cmyk
C                                                                       4
M                                                                       0
Y                                                                      36
K                                                                       9
NEIGHBOUR_STR           PMS586[775][226,229,132](3.6):hypnotic[4592][2...
NUM_NEIGHBOURS_MAXDE                                                    4
WORD_TAGS               [light, PMS586, hypnotic, jonquil, green, lime...
Name: 5000, dtype: object
```

## Known Bugs:
  - I don't know of any right now, but I'm sure they exist!

## Ideas
  - Allow user to enter a listindex as an argument to show_color(), so that they can select what to show if there are multiple options

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
