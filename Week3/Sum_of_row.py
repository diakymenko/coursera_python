n = int(input())
sum = 0
while n != 0:
    sum = (1 / n ** 2) + sum
    n = n - 1
print(sum)
