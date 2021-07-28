# ColorController.py

Welcome to the ColorController Python library! 

My name is Tal Zaken, and I wrote this library for use in a natural language processing project 
that aims to take in free-form text, and spit out color data which somehow relates to the text's 
content. 

Enough about that. Here are some things that you can do with ColorController:

## 1. Encode color data in various formats.
####Example 1: Create a ColorController object using a familiar, english-language color name.
You can set a color using a very large library of color names. 
See the colornames.txt document contained herein, with enormous thanks to 
[Martin Krzywinski](http://mkweb.bcgsc.ca/colornames). 

The following code:
```python
from ColorController import ColorController

c = ColorController(name='yellow')

print(f"Name: {c.name}", 
      f"Hex Code: {c.hex_code}", 
      f"RGB: {c.rgb}", 
      f"HSV: {c.hsv}", 
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
c.name = 'blue'

print(f"Name: {c.name}", 
      f"Hex Code: {c.hex_code}", 
      f"RGB: {c.rgb}", 
      f"HSV: {c.hsv}", 
      sep='\n')
```
You will see that all properties have updated:
```
Name: blue
Hex Code: ['#00008B', '#0000CD', '#0000EE', '#0000FF', '#0087BD', '#0093AF', '#0018A8', '#0247FE', '#0343DF', '#1F75FE', '#2242C7', '#333399']
RGB: (51, 51, 153)
HSV: (0.6666666666666666, 0.6666666666666666, 153)
```
Notably, the colornames.txt file has numerous entries that share the name "blue." This is true of many colors.
Because color is thought to be a culturally relative phenomenon, I have chosen to return all 

## 2. Modify a color, and keep track of changes to the color in all available formats.
## 3. Show a color. 
## 4. Invert a color.

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

## Notes:
  - To lighten a color in HSV, one can push the saturation toward zero
  - To darken a color in HSV, one can push the value toward zero

## Ideas:
  - Create a Color class, which manages name, hex, rgb, and hsv for us. Whenever one is updated, update the others.
  - Implement a way to measure the distance between two colors, given their RGB values. This will help: https://www.compuphase.com/cmetric.htm   