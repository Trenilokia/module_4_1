from math import inf
def divide(first, second):
    res = None
    if second != 0:
        res = first / second
    else:
        return inf
    return res
