x1, y1, x2, y2, x3, y3 = float(input()), float(input()), float(input()), float(
    input()), float(input()), float(input())


def count_distance(x1, y1, x2, y2):
    a = abs(x1 - x2)  # module of the number, optional since we do **2
    # as the next step
    b = abs(y1 - y2)
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c


a = count_distance(x1, y1, x2, y2)
b = count_distance(x2, y2, x3, y3)
c = count_distance(x1, y1, x3, y3)
p = a + b + c

print(p)
