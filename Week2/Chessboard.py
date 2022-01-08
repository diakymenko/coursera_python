a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = (a + b) % 2 == 0
m = (c + d) % 2 == 0
if (k and m) or (not k and not m):
    print("YES")
else:
    print("NO")
