n = int(input())
if n >= 3 and ((n % 5) % 3 == 0 or (n % 3) % 5 == 0 or (n % 8) % 3 == 0 or (
        n % 8) % 5 == 0 or (n - 3) % 5 == 0 or (n - 5) % 3 == 0 or (
                       n - 8) % 3 == 0 or (n - 8) % 5 == 0):
    print("YES")
else:
    print("NO")
