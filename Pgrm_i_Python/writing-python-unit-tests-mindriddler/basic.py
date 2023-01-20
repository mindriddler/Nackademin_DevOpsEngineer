def line(x, k=1, m=5):
    result = k*x + m
    return result


def diff_twist(x, y):
    result = x - y
    if x > 0:
        return result
    return 0


def add_multiply(x, y):
    add_result = x + y
    multiply_result = add_result * 2
    return multiply_result
