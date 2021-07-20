# TextToColor
This repo will be used to explore methods for converting text strings into color hexadecimal codes. 


Resources:
  - What is color?: https://www.crayola.com/for-educators/resources-landing/articles/color-what-is-color.aspx
  - unofficial crayola colors: https://www.w3schools.com/colors/colors_crayola.asp
  - color names database: http://mkweb.bcgsc.ca/colornames/
  - interactive color code tool: https://www.hexcolortool.com/#3cec71
  - NLTK Information extraction chapter: http://www.nltk.org/book/ch07.html
  - colorsys source code: https://github.com/python/cpython/blob/3.9/Lib/colorsys.py

Notes:
To properly lighten a color, I believe that I need to return a value that is somewhere between the min and max values of RGB. So, while 255 is a theoretical lightness ceiling, if a specific color has no RGB value that equals 255, this is an invalid lightness factor.
