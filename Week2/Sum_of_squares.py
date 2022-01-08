n = int(input())
sum = n ** 2
k = 1
while k < n:
    sum += k ** 2
    k = k + 1
print(sum)
