n = int(input())
times_lst = [1, 3, 0, 0, 2, 0, 1]
points_list = [210, 200, 200, 200, 150, 150, 120]
sum_numbers = 0
min_points = 0
for i in range(len(times_lst)):
    if sum_numbers + times_lst[i] < n:
        sum_numbers += times_lst[i]
    else:
        if n == 1:
            min_points = points_list[i]
        else:
            min_points = points_list[i-1]
        break

print(min_points)