def power(a, n):
    if n == 0:
        return 1
    res = a * power(a, n - 1)
    return res


a, n = float(input()), float(input())
print(power(a, n))
