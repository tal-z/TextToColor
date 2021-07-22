# TextToColor
This repo will be used to explore methods for converting text strings into color hexadecimal codes. 


## Resources:
  - What is color?: https://www.crayola.com/for-educators/resources-landing/articles/color-what-is-color.aspx
  - unofficial crayola colors: https://www.w3schools.com/colors/colors_crayola.asp
  - color names database: http://mkweb.bcgsc.ca/colornames/
  - interactive color code tool: https://www.hexcolortool.com/#3cec71
  - NLTK Information extraction chapter: http://www.nltk.org/book/ch07.html
  - colorsys source code: https://github.com/python/cpython/blob/3.9/Lib/colorsys.py
  - explanation of calculating distance in hsv space: https://stackoverflow.com/questions/35113979/calculate-distance-between-colors-in-hsv-space

## Notes:
  - To lighten a color in HSV, one can push the saturation toward zero
  - To darken a color in HSV, one can push the value toward zero

## Ideas:
  - Create a Color class, which manages name, hex, rgb, and hsv for us. Whenever one is updated, update the others.
  - Implement a way to measure the distance between two colors, given their RGB values. This will help: https://www.compuphase.com/cmetric.htm   