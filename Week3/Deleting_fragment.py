s = input()
left = s.find("h")
right = len(s) - 1 - s[::-1].find("h")
s1 = s[:left]
s2 = s[right + 1:]
print(s1 + s2)
