def circle(r):
    pi = 3.14
    res = pi * r ** 2
    return res


def rect(side):
    res = side * 4
    return res


def square(fig: int, attr: int) -> float:
    if fig == 1:
        return circle(attr)
    elif fig == 2:
        res = rect(attr)
        return res

a = square(1, 7)
print(a)
