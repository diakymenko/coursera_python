from math import sqrt

a, b, c = float(input()), float(input()), float(input())
if a == b == c == 0:
    print(3)
elif a == 0 and b != 0:
    print(1, - c / b)
elif a == 0 and b == 0:
    print(0)
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        if x1 < x2:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
    elif D == 0:
        x1 = - b / (2 * a)
        print(1, x1)
    else:
        print(0)
