class House:
    def __init__(self, name, number1):
        self.name = name
        self.number_of_floors = number1

    def go_to(self, new_floor):
        i = 1
        list_of_floor = list(range(1, new_floor+1))
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in list_of_floor:
                if i != new_floor:
                    print(i)
                else:
                    break
            print(new_floor)
h1 = House('ЖК Пупа', 19)
h1.go_to(7)
h2 = House('ЖК Лупа', 9)
h2.go_to(14)