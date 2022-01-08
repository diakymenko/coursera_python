n = int(input())
m = int(input())
k = int(input())
if ((n <= m) and (k % n == 0 or k % m == 0) and (k <= n * m - n)) or (
        (n > m) and (k % m == 0 or k % n == 0) and (k <= n * m - m)):
    print("YES")
else:
    print("NO")
