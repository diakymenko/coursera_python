n = int(input())
sum = n
k = 0
while n != 0:
    k += 1
    n = int(input())
    sum += n
    av = (sum) / k
print(av)
