n = int(input())
a = n % 10
if 10 < n < 20 or n % 10 == 0 or 5 <= a <= 9:
    print(n, "korov")
elif a == 1:
    print(n, "korova")
else:
    print(n, "korovy")
