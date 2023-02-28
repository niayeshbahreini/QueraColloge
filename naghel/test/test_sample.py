import unittest
from vehicle import Vehicle
from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle
from airplane import Airplane, B707


class InheritanceTest(unittest.TestCase):

    def test_vehicle(self):
        v = Vehicle(name="Car", price=5000, number_of_seats=5, max_speed=280)
        self.assertEqual(v.name, "Car", '\nدر تابع سازنده کلاس Vehicle، نام وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.price, 5000, '\nدر تابع سازنده کلاس Vehicle، قیمت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_seats, 5, '\nدر تابع سازنده کلاس Vehicle، تعداد صندلی‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.max_speed, 280, '\nدر تابع سازنده کلاس Vehicle، بیشینه سرعت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')

    def test_ground_vehicle(self):
        v = GroundVehicle(name="Bicycle", price=100, number_of_seats=1, max_speed=60, number_of_wheels=2,
                          steering_wheel="Manual")
        self.assertTrue(issubclass(GroundVehicle, Vehicle), '\nکلاس GroundVehicle باید از کلاس Vehicle ارث‌بری کند.')
        self.assertFalse(issubclass(GroundVehicle, FlyingVehicle), '\nکلاس GroundVehicle نباید از کلاس FlyingVehicle ارث‌بری کند.')
        self.assertEqual(v.name, "Bicycle", '\nدر تابع سازنده کلاس GroundVehicle، نام وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.price, 100, '\nدر تابع سازنده کلاس GroundVehicle، قیمت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_seats, 1, '\nدر تابع سازنده کلاس GroundVehicle، تعداد صندلی‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.max_speed, 60, '\nدر تابع سازنده کلاس GroundVehicle، بیشینه سرعت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_wheels, 2, '\nدر تابع سازنده کلاس GroundVehicle، تعداد چرخ‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.steering_wheel, "Manual", '\nدر تابع سازنده کلاس GroundVehicle، فرمان وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')

    def test_flying_vehicle(self):
        v = FlyingVehicle(name="Airplane", price=500000, number_of_seats=300, max_speed=400, fuel="Oil",
                          number_of_fins=2)
        self.assertTrue(issubclass(FlyingVehicle, Vehicle), '\nکلاس FlyingVehicle باید از کلاس Vehicle ارث‌بری کند.')
        self.assertFalse(issubclass(FlyingVehicle, GroundVehicle), '\nکلاس FlyingVehicle نباید از کلاس GroundVehicle ارث‌بری کند.')
        self.assertEqual(v.name, "Airplane", '\nدر تابع سازنده کلاس FlyingVehicle، نام وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.price, 500000, '\nدر تابع سازنده کلاس FlyingVehicle، قیمت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_seats, 300, '\nدر تابع سازنده کلاس FlyingVehicle، تعداد صندلی‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.max_speed, 400, '\nدر تابع سازنده کلاس FlyingVehicle، بیشینه سرعت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.fuel, "Oil", '\nدر تابع سازنده کلاس FlyingVehicle، سوخت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_fins, 2, '\nدر تابع سازنده کلاس FlyingVehicle، تعداد پره‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')

    def test_airplane(self):
        v = Airplane(name="Airplane", price=500000, number_of_seats=300, max_speed=400, number_of_wheels=10,
                     steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                     captain="Bagher")
        self.assertTrue(issubclass(Airplane, Vehicle), '\nکلاس Airplane باید از کلاس Vehicle ارث‌بری کند.')
        self.assertTrue(issubclass(Airplane, FlyingVehicle), '\nکلاس Airplane باید از کلاس FlyingVehicle ارث‌بری کند.')
        self.assertTrue(issubclass(Airplane, GroundVehicle), '\nکلاس Airplane باید از کلاس GroundVehicle ارث‌بری کند.')
        self.assertEqual(v.name, "Airplane", '\nدر تابع سازنده کلاس Airplane، نام وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.price, 500000, '\nدر تابع سازنده کلاس Airplane، قیمت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_seats, 300, '\nدر تابع سازنده کلاس Airplane، تعداد صندلی‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.max_speed, 400, '\nدر تابع سازنده کلاس Airplane، بیشینه سرعت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_wheels, 10, '\nدر تابع سازنده کلاس Airplane، تعداد چرخ‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.steering_wheel, "Manual", '\nدر تابع سازنده کلاس Airplane، فرمان وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.fuel, "Oil", '\nدر تابع سازنده کلاس Airplane، سوخت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_fins, 2, '\nدر تابع سازنده کلاس Airplane، تعداد پره‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.airline, "Quera Air", '\nدر تابع سازنده کلاس Airplane، نام خط‌ هوایی وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_crew, 65, '\nدر تابع سازنده کلاس Airplane، تعداد مهمانداران وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.captain, "Bagher", '\nدر تابع سازنده کلاس Airplane، نام کاپیتان وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')

    def test_b_707(self):
        v = B707(name="SAliB", price=850000, number_of_seats=850, max_speed=500, number_of_wheels=18,
                 steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                 captain="Bagher")
        self.assertTrue(issubclass(B707, Vehicle), '\nکلاس B707 باید از کلاس Vehicle ارث‌بری کند.')
        self.assertTrue(issubclass(B707, FlyingVehicle), '\nکلاس B707 باید از کلاس FlyingVehicle ارث‌بری کند.')
        self.assertTrue(issubclass(B707, GroundVehicle), '\nکلاس B707 باید از کلاس GroundVehicle ارث‌بری کند.')
        self.assertTrue(issubclass(B707, B707), '\nکلاس B707 باید از کلاس B707 ارث‌بری کند.')
        self.assertEqual(v.name, "SAliB", '\nدر تابع سازنده کلاس B707، نام وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.price, 850000, '\nدر تابع سازنده کلاس B707، قیمت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_seats, 850, '\nدر تابع سازنده کلاس B707، تعداد صندلی‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.max_speed, 500, '\nدر تابع سازنده کلاس B707، بیشینه سرعت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_wheels, 18, '\nدر تابع سازنده کلاس B707، تعداد چرخ‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.steering_wheel, "Manual", '\nدر تابع سازنده کلاس B707، فرمان وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.fuel, "Oil", '\nدر تابع سازنده کلاس B707، سوخت وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_fins, 2, '\nدر تابع سازنده کلاس B707 تعداد پره‌ها وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.airline, "Quera Air", '\nدر تابع سازنده کلاس B707، نام خط‌ هوایی وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.number_of_crew, 65, '\nدر تابع سازنده کلاس B707، تعداد مهمانداران وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(v.captain, "Bagher", '\nدر تابع سازنده کلاس B707 نام کاپیتان وسیله نقلیه را به درستی مقداردهی نمی‌کنید.')


if __name__ == '__main__':
    unittest.main()