s = input()
n1 = s.find("h")
n2 = s.rfind("h")
first_piece = s[:n1 + 1]
third_piece = s[n2:]
s3 = s[n1 + 1:n2]
second_piece = s3.replace("h", "H")
s = first_piece + second_piece + third_piece
print(s)
