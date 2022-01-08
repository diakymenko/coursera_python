def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == 0 and b == 0:
        return 0
    else:
        a = a + 1
        b = b - 1
        total = a
        if b != 0:
            return sum(a, b)
        return total


a, b = int(input()), int(input())
print(sum(a, b))
