from math import sqrt

a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (- b + sqrt(D)) / (2 * a)
    x2 = (- b - sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
if D == 0:
    x1 = (- b + sqrt(D)) / (2 * a)
    print(x1)