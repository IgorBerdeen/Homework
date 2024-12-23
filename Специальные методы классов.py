class House:
    def __init__(self, name, number1):
        self.name = name
        self.number_of_floors = number1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f"Название: {self.name}, количество этажей: {self.number_of_floors}")

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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))