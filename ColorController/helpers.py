
def unlist(data):
    if data == []:
        return ''
    elif type(data) == list:
        return data[-1]
    else:
        return data
