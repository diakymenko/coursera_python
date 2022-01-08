s = input()
left = s.find("h")
right = len(s) - 1 - s[::-1].find('h')
s1 = s[:left + 1]
s2 = s[left + 1:right]
s3 = s[right:]
print(s1 + s2 * 2 + s3)
