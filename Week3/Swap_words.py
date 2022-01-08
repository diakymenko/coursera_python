string = input()
blank = string.find(' ')
a = string[:blank]
b = string[blank + 1:]
print(b, a)


