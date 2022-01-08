lst = list(map(int, input().split()))
min_elem = lst[0]
max_elem = lst[0]
index_min = 0
index_max = 0

for i in range(len(lst)):
    if lst[i] < min_elem:
        min_elem = lst[i]
        index_min = i
    if lst[i] > max_elem:
        max_elem = lst[i]
        index_max = i

lst[index_min] = max_elem
lst[index_max] = min_elem
print(' '.join(map(str, lst)))
