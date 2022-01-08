mylist = list(map(int, input().split()))
min_num = 1000
for i in range(1, len(mylist)):
    if mylist[i] > 0 and mylist[i] <= min_num:
        min_num = mylist[i]
print(min_num)
