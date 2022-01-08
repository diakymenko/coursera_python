n = int(input())
print(("+___ ") * n, end="")
print("")
for i in range(n):
    print("|" + str(i + 1) + " / ", end="")
print("")
print(("|__\ ") * n, end="")
print("")
print(("|    ") * n, end="")
