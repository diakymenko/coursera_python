n = int(input())
lst = list(map(int, input().split()))
n = int(input())
closest_num = lst[0]
dif = abs(n - closest_num)
for i in range(1, len(lst)):
    new_dif = abs(n - lst[i])
    if dif > new_dif:
        dif = new_dif
        closest_num = lst[i]
print(closest_num)
