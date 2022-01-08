class Human:
    default_name = "John"
    default_age = 20

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(
            f"My name is {self.name}. I'm {self.age}. I have {self.__money} and a {self.__house}")

    def __make_deal(self, price, house):
        self.__money -= price
        self.__house = house

    def earn_money(self, income):
        self.__money += income
        print(f"Now {self.name} has ${self.__money}.")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if final_price > self.__money:
            print("Not enough money")
        else:
            self.__make_deal(final_price, house)

    @staticmethod
    def default_info():
        print(
            f"My default name is {Human.default_name}. My default age is {Human.default_age}")


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price - self._price / 100 * discount
        print(final_price)
        return final_price

    def __str__(self):
        return f'house price: {self._price}, size: {self._area}'


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)
