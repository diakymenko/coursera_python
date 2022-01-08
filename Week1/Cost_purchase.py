a = int(input())
b = int(input())
n = int(input())
k = (a * 100 + b) * n
m = k % 100
l = k // 100
print(l, m)
