from math import sqrt


def is_square_sum(n):
    a = n
    if n == 0:
        return True
    while n > 0:
        sq = sqrt(n)
        remainder = sq - int(sq)
        if remainder == 0:
            dif = a - n
            d = sqrt(dif)
            if d - int(d) == 0:
                return True
            n = n - 1
        n = n - 1
    return False


print(is_square_sum(999990999))

