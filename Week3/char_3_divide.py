s = input()
x = 0
new_str = ""
while x < len(s):
    if x % 3 != 0:
        new_str += s[x] #we add only those characters which
        # indexes are not divided by 3
    x += 1
print(new_str)


