s = input()
index_first = s.find("f")
if index_first != -1:
    reversed = s[::-1]
    index_last = (len(s) - 1) - reversed.find("f")
    if index_first == index_last:
        print(index_first)
    else:
        print(index_first, index_last)
