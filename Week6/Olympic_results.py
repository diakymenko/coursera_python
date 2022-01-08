def max_index(lst):
    return int(lst[1])


n = int(input())
new_lst = []

for i in range(n):
    lst = input().split()
    new_lst.append(lst)
new_lst.sort(key=max_index, reverse=True)
for lst in new_lst:
    print(lst[0])
