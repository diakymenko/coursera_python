def mindivisor(n):
    i = 2
    q = n ** (1 / 2)
    while i <= q:
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())
print(mindivisor(n))