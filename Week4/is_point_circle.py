def point(a, b, c, d, e):
    return (a - c) ** 2 + (b - d)**2 <= e**2


x, y, xc = float(input()), float(input()), float(input())
yc, r = float(input()), float(input())
if point(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
