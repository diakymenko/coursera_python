n = int(input())
count = 1
first = 0
while n != 0:
    if n > first:
        count = 1
        first = n
    elif n == first:
        count += 1
    n = int(input())
print(count)
