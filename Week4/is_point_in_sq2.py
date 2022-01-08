def isPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


x1, y1 = float(input()), float(input())
if isPointInSquare(x1, y1):
    print("YES")
else:
    print("NO")
