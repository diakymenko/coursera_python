n = int(input())
x = 2
while n % x > 0:
    x = x + 1
if n % x == 0:
    print(x)
