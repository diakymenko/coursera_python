n = int(input())
a = n % 10
b = (n // 10) % 10
c = (n // 100) % 10
d = (n // 1000) % 10
right = str(b) + str(a)
left = str(c) + str(d)
e = (int(left) - int(right)) + 1
print(e)
