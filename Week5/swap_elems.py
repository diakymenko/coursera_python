lst = list(map(int, input().split()))
for i in range(0, (len(lst) - 1), 2):
    first = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = first
print(' '.join(map(str, lst)))
