from sys import stdin
class Matrix_error(BaseException):
    def __init__(self, Matrix, other):
        self.arg1 = Matrix
        self.arg2 = other

    def __str__(self):
        return 'спать'

class Matrix:
    def __init__(self, input_list):
        self.__list = []
        for sublist in input_list:
            a = sublist.copy()
            self.__list.append(a)

    def __str__(self):
        result = ""
        for sublist in self.__list:
            result += '\t'.join(map(str, sublist)) + "\n"
        return result[:-1]

    def size(self):
        return len(self.__list), len(self.__list[0])

    def __add__(self, other):
        sum_list = []

        l1 = self.__list
        l2 = other.__list

        for i in range(len(l1)):
            sublist = []
            for j in range(len(l1[i])):
                sum = l1[i][j] + l2[i][j]
                sublist.append(sum)
            sum_list.append(sublist)
        return Matrix(sum_list)

    def __mul__(self, multiplier):
        if isinstance(multiplier, int):
            mult_list = []
            for i in range(len(self.__list)):
                sublist = []
                for j in range(len(self.__list[i])):
                    result = self.__list[i][j] * multiplier
                    sublist.append(result)
                mult_list.append(sublist)
        else:
            raise Matrix_error(self, multiplier)
        return Matrix(mult_list)

    __rmul__ = __mul__


#exec(stdin.read())
m = Matrix([[10, 10], [0, 0], [1, 1]])
#print(m)

try:
    print(n * 'ksjdghjf')

except BaseException as dasha:
    pass
