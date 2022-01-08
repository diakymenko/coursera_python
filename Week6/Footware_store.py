n = int(input())
if n <= 100:
    sizes = list(map(int, input().split()))
    sizes.sort()
    pointer = n
    a = 0
    for i in sizes:
        if i >= pointer:
            pointer = i + 3
            a += 1
    print(a)
