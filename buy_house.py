class Human:

    default_name: str | None = None
    default_age: int | None = None

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    @staticmethod
    def default_info() -> None:
        print(f'\nDefault name is - {Human.default_name}'
              f'\nDefault age is - {Human.default_age}')

    def __make_deal(self, home_obj_finished: 'House', cost: int | float) -> None:
        self.__money -= cost
        self.__house = home_obj_finished

    def earn_money(self, value: int | float) -> None:
        self.__money += value
        print(f'Пополнение счёта на: {value}')

    def buy_house(self, home_obj: 'House', discount: int | float) -> None:
        house_price: float = home_obj.final_price(discount)

        if self.__money < house_price:
            raise ValueError('Недостаточно средств на счету!')

        self.__make_deal(home_obj_finished=home_obj, cost=house_price)

    def __str__(self) -> str:
        return (f'\nИмя: {self.name}'
                f'\nВозраст: {self.age}'
                f'\nДом: {self.__house}'
                f'\nСредства = {self.__money}')


class House:

    def __init__(self,
                 area: str,
                 price: int | float) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: int | float) -> int | float:
        return self._price - (self._price * (discount / 100))

    def __str__(self):
        return f'Площадь - {self._area}, Цена - {self._price}'


class SmallHouse(House):

    def __init__(self, small_area='40м2', small_price=500) -> None:
        self._area = small_area
        self._price = small_price
        super().__init__(area=small_area, price=small_price)


Vahe = Human('Vahe', 25)
house = House('100m2', 1000)
small = SmallHouse()

Vahe.default_info()
print('--------', end='')
print(Vahe)
Vahe.earn_money(2000)
Vahe.buy_house(small, 50)
print(Vahe)
Vahe.buy_house(house, 43)
print(Vahe)
