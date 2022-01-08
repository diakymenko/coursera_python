def mindivisor(n):
    i = 2
    q = n ** (1 / 2)
    while i <= q:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
if mindivisor(n):
    print("YES")
else:
    print("NO")