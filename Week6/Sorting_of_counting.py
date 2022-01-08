list = list(map(int, input().split()))


def CountSort(list):
    counter = [0] * 101
    for elem in list:
        counter[elem] += 1
    list.clear()
    for i in range(len(counter)):
        if counter[i] != 0:
            times = counter[i]
            number = i
            for i in range(times):
                list.append(number)


CountSort(list)
print(' '.join(map(str, list)))
