def min_4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    min_4 = min(min1, min2)
    return min_4


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min_4(a, b, c, d))
