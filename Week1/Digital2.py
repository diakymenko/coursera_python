n = int(input())
hours = n // 3600 % 24
b = n % 3600
m = b // 60
m1 = m // 10
m2 = m % 10
s = b % 60
s1 = s // 10
s2 = s % 10
print(hours, str(m1) + str(m2), str(s1) + str(s2), sep=":")
