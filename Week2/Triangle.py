x, y, z = int(input()), int(input()), int(input())
if x >= z and x >= y:
    max = x
    a = y
    b = z
elif y >= x and y >= z:
    max = y
    a = x
    b = z
else:
    max = z
    a = x
    b = y
if max >= a + b:
    print("impossible")
else:
    if max ** 2 == a ** 2 + b ** 2:
        print("rectangular")
    elif max ** 2 < a ** 2 + b ** 2:
        print("acute")
    else:
        print("obtuse")
