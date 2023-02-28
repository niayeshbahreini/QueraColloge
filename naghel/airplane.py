# Your imports goes here
from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle


class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        super().__init__(**kwargs)


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)