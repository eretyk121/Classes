class Animals():
    def __init__(self, type, name, weight):
        self.type = type
        self.weight = weight
        self.name = name

    def feed(self):
        print(f'{self.name.title()} кушает')

class Cow(Animals):
    def __init__(self, type, name, weight):
        super().__init__(type, name, weight)

    def milk(self):
        print(f'{self.name.title()} дает молоко')

    def voice(self):
        print(f'{self.name.title()} издает звук "Мууууу"')
cow_1 = Cow("Корова", "Манька", 400)

class Goat(Cow):
    def __init__(self, type, name, weight):
        super().__init__(type, name, weight)

    def voice(self):
        print(f'{self.name.title()} издает звук "Бееееее"')
goat_1 = Goat("Коза", "Рога", 70)
goat_2 = Goat("Коза", "Копыта", 80)

class Goose(Animals):
    def __init__(self, type, name, weight):
        super().__init__(type, name, weight)

    def voice(self):
        print(f'{self.name.title()} издает звук "Га-га-га"')

    def eags(self):
        print('К сожалению гуси не несут яйца :(')
goose_1 = Goose("Гусь", "Серый", 12)
goose_2 = Goose("Гусь", "Белый", 14)

class Duck(Goose):
    def __init__(self, type, name, weight):
        super().__init__(type, name, weight)

    def eags(self):
        print(f'Собрал яйца, уоторые снесла {self.name.title()}')

    def voice(self):
        print(f'{self.name.title()} издает звук "Кря-кря"')
duck_1 = Duck("Утка", "Кряква", 5)

class Sheep(Animals):
    def __init__(self, type, name, weight):
        super().__init__(type, name, weight)

    def voice(self):
        print(f'{self.name.title()} издает звук "Ме-е-е-е-е"')

    def cute(self):
        print(f'Подстриг шерсть у овцы по имени {self.name.title()}')
sheep_1 = Sheep("Овца", "Барашек", 90)
sheep_2 = Sheep("Овца", "Кудрявый", 100)

weight_list = {cow_1.name: cow_1.weight, goat_1.name: goat_1.weight, goat_2.name: goat_2.weight, goose_1.name: goose_1.weight,
               goose_2.name: goose_2.weight, duck_1.name: duck_1.weight, sheep_1.name: sheep_1.weight, sheep_2.name: sheep_2.weight}

max_weight = max(weight_list.values())
sum_weight = sum(weight_list.values())
print(f'Общая масса всех животных: {sum_weight}')

for name, weight in weight_list.items():
    if weight == max_weight:
        print(f'Самое тяжелое животное: {name}')