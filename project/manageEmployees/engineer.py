import math

from person import Person, Consts


class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.work_place = None
        self.age = age
        self.job = "engineer"

    def get_price(self):
        price = math.floor(Consts.BASE_PRICE.get("engineer") * math.sqrt(Consts.MIN_AGE / self.age))
        return price

    def calc_life_cost(self):
        costs = math.floor(Consts.BASE_COST.get("engineer") * math.sqrt(self.age / Consts.MIN_AGE))
        return costs

    def calc_income(self):
        income = math.floor(Consts.BASE_INCOME["engineer"][self.work_place.get_expertise()] * math.sqrt(Consts.MIN_AGE / self.age))
        return income