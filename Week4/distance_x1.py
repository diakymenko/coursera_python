x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def count_distance(x1, y1, x2, y2):
    a = abs(x1 - x2) #module of the number, optional since we do **2
    # as the next step
    b = abs(y1 - y2)
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c


print(count_distance(x1, y1, x2, y2))
