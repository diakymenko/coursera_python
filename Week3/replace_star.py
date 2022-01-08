s = input()
x = 0
s_left = ""
while x < len(s):
    sub_str = s[x] + "*"
    s_left = s_left + sub_str
    x += 1
print(s_left[:len(s_left) - 1])
