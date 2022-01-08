a, b, c = int(input()), int(input()), int(input())
if (a + b) % 2 != 0 or (b + c) % 2 != 0 or (a + c) % 2 != 0:
    print('YES')
else:
    print("NO")
