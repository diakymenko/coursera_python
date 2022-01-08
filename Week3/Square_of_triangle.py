from math import sqrt

a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
s = float('{0:.6f}'.format(s))
print(s)
