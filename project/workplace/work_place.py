class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 300, 'school': 100, 'company': 200}
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10


class WorkPlace:
    instances = []

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = list()
        self.capacity = 1
        self.instances.append(self)

    def get_price(self):
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.calc_capacity()
        self.level += 1

    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            person.work_place = self
            self.employees.append(person)

    def get_expertise(self):
        return self.expertise

    def calc(self):
        return (self.calc_costs()) * -1

    @staticmethod
    def calc_all():
        total = 0
        for instance in WorkPlace.instances:
            total += instance.calc()
        return total