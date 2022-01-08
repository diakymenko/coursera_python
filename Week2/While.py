# n = int(input())
# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10
# print(sum)
now = int(input())
nowMin = now
while now != 0:
    if now < nowMin:
        nowMin = now
print(nowMin)






