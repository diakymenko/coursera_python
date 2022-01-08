a = int(input())
b = int(input())
c = (b - a) + 1
d = (a - 1) % c
e = b % c
if d == 0 and e == 0:
    print("YES")
else:
    print("NO")
