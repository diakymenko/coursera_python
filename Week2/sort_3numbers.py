a, b, c = int(input()), int(input()), int(input())
if a <= b <= c:
    print(a, b, c)
elif b <= a <= c:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif a <= c <= b:
    print(a, c, b)
elif b <= c <= a:
    print(b, c, a)
else:
    print(c, b, a)
