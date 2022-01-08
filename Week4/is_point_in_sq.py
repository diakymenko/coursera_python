def isPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


x1, y1 = float(input()), float(input())
if isPointInSquare(x1, y1):
    print("YES")
else:
    print("NO")
