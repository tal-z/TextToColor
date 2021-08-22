import math

def unlist(data):
    if data == []:
        return ''
    elif type(data) == list:
        return data[-1]
    else:
        return data


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

