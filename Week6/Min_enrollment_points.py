inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

n = int(inFile.readline())   #returns first line
points_list = []

for line in inFile:
    lst = line.split() #create a list for with each line elements
    is_valid = True
    for item in lst[-3:]:
        if int(item) < 40: #filter out those whose exam score is less than 40
            is_valid = False
    if is_valid:
        sum_numbers = int(lst[len(lst) - 1]) + int(lst[len(lst) - 2]) + int(
            lst[len(lst) - 3]) #we need the last 3 digits of each line to get a sum of scores
        points_list.append(sum_numbers)

points_list.sort(reverse=True)

students = len(points_list)

max_points = points_list[0]
counter = 0
for point in points_list: # to know the number of max scores
    if point == max_points:
        counter += 1


times_lst = [0] * len(points_list) # to create a list of zeros and populate it with the
                                # of times we have each score
number = 0
index = 0

for i in range(len(points_list)):
    if points_list[i] == number:
        times_lst[index] += 1 #index remains the same if we find the same number as previous
    else:
        times_lst[i] += 1
        number = points_list[i] #new value is assigned to number
        index = i #index is modified only if a new number is found

#this method sums up times each number was found until the limit of available spots (n) is reached
sum_numbers = 0
min_points = 0
for i in range(len(times_lst)):
    if sum_numbers + times_lst[i] <= n: #sums up until the sum is less than n
        sum_numbers += times_lst[i]
    else:
        if i == 0:
            min_points = points_list[i] #if i stopped at 0 index, it should take 0 index in points_list too
        else:
            min_points = points_list[i - 1] #if sum is greater than n, the current index is greater than the one that still fits
                                            # so we need to take a previous index
        break #we don't need the prgm to run further

if n == students:
    print(0, file=outFile)
elif counter > n:
    print(1, file=outFile)
else:
    print(min_points, file=outFile)
inFile.close()
outFile.close()
print(points_list)