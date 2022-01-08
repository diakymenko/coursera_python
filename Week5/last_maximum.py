mylist = list(map(int, input().split()))
max_value = mylist[0]
for i in range(len(mylist)):
    if mylist[i] > max_value:
        max_value = mylist[i]
    if mylist[i] == max_value:
        index = i
print(max_value, index)
