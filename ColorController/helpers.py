import math

def unlist(object):
    """Take some object, and checks if it is a list.
    If it is a list, it returns the last value in the list, or an empty string if the list is empty.
    Else, it returns the object unmodified."""
    if object == []:
        return ''
    elif type(object) == list:
        return object[0]
    else:
        return object


def hsv_round(n, decimals=0):
    """
    Custom round function to return a value rounded to the correct number of decimals.
    In the case of HSV360, this is zero decimals (integer).
    This custom round function works differently than the built-in round() function. It breaks ties by rounding up,
    whereas the built-in round() function breaks ties by rounding to the nearest even number.

    See this primer on rounding in Python: https://realpython.com/python-rounding/
    """
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

