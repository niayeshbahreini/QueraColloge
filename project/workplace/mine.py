import math

from work_place import WorkPlace, Consts


class Mine(WorkPlace, Consts):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "mine"


    def calc_capacity(self):
        self.capacity = math.pow(int(self.level), 2)
        return self.capacity


    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST + (Consts.LEVEL_MUL * self.level))
        return costs