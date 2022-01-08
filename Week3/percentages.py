p, x, y = int(input()), int(input()), int(input())
sum_1 = (x * 100 + y) / 100 * p + (x * 100 + y)
sum_rub = sum_1 // 100
sum_coin = sum_1 % sum_rub

print(int(sum_rub), int(sum_coin))
