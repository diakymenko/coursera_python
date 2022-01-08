n = int(input())
sequence = n
counter = 0
max_digits_in_row = 0
while n != 0:
    if n == sequence:
        counter += 1
    else:
        sequence = n
        counter = 1
    max_digits_in_row = max(max_digits_in_row, counter)
    n = int(input())
print(max_digits_in_row)
