n = int(input())
if n <= 10 ** 5:
    list = list(map(int, input().split()))
    list.sort()
    print(' '.join(map(str, list)))
