def reverse(lst, i):
    if i < len(lst) // 2:
        a = lst[i]
        lst[i] = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = a
        i += 1
        reverse(lst,i)
    return lst




lst = [1,2,3,6]
lst2 = reverse(lst,0)

print(lst2)

#abcd
#dcba