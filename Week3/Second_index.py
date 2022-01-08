string = input()
pos = string.find("f")
if pos != -1:
    a = string.find("f", pos + 1)
    print(a)
else:
    print(-2)

