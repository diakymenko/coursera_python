max_storage = list(map(int, input().split()))
number_of_users = max_storage[1]
user_data = []
for i in range(number_of_users):
    user_data.append(int(input()))
user_data.sort()
sum = 0
counter = 0
index = 0
while sum < max_storage[0] and index < number_of_users:
    sum += user_data[index]
    index += 1
    if sum <= max_storage[0]:
        counter += 1
print(counter)
