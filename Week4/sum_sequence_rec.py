def sequence():
    sum = 0
    n = int(input())
    if n != 0:
        sum = n + sequence()
    return sum

print(sequence())
