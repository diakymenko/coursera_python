from Coursera_Python.Week9.human import Human, House, SmallHouse

human1 = Human("Dasha",33)
human2 = Human()

human1.age = 28

human1.info()
human2.info()

Human.default_info()
human1.earn_money(600)
human1.info()

house1 = House(2500, 500)
human1.buy_house(house1, 20)
human1.info()

smallhouse1 = SmallHouse(100)
human2.buy_house(smallhouse1, 100)
human2.info()
