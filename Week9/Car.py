class Car:

    __hp = 1000

    def __init__(self, color):
        self.__color = color

    def get_car_info(self):
        return self.__color + ' ' + str(self.__hp)

    @staticmethod
    def honk():
        print('Beep beep')
