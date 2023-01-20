def add(x, y):
    result = x + y + 5
    return result


def diff(x, y):
    result = x - y
    if x > 0:
        return result
    elif x < -50:
        return 888
    return 0
