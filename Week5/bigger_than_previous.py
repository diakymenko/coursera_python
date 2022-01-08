mylist = list(map(int, input().split()))
prev = mylist[0]
for i in range(1, len(mylist)):
    if mylist[i] > prev:
        print(mylist[i], end=" ")
    prev = mylist[i]
