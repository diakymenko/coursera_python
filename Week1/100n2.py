"""n = input()
a = n * 100
b = int(a) ** 2
print(b)"""
MAX_NUMBER = 100
number = number_in_a_row(type)
type = define_type(i)

def number_in_a_row (type):
    for i in range(1, MAX_NUMBER + 1):
        return i

def define_type(i):
    if i % 2 == 0:
        type = "even"
    else: type = "odd"
    print(i, "is", type)
    return type

