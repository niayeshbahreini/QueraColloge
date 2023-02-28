import math

from work_place import WorkPlace, Consts


class Company(WorkPlace, Consts):
    def __init__(self,name):
        super().__init__(name)
        self.expertise = "company"

    def calc_capacity(self):
        self.capacity = int(self.level)
        return self.capacity

    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST * self.level)
        return costs