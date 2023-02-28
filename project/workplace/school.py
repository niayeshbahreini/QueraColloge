import math

from work_place import *


class School(WorkPlace,Consts):
    def __init__(self,name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = int(math.floor(math.sqrt(self.level)))
        return self.capacity

    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST * int(math.floor(math.sqrt(self.level))))
        return costs