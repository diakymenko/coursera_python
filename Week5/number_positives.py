mylist = list(map(int, (input().split())))
a = 0
for i in range(len(mylist)):
    if mylist[i] > 0:
        a += 1
print(a)
