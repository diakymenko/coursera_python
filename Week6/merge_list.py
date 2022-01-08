lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = []
index1 = 0
index2 = 0

while index1 < len(lst1) and index2 < len(lst2):
    if lst1[index1] <= lst2[index2]:
        lst3.append(lst1[index1])
        index1 += 1
    else:
        lst3.append(lst2[index2])
        index2 += 1
if index1 >= len(lst1):
    while index2 < len(lst2):
        lst3.append(lst2[index2])
        index2 += 1
if index2 >= len(lst2):
    while index1 < len(lst1):
        lst3.append(lst1[index1])
        index1 += 1
print(' '.join(map(str, lst3)))
