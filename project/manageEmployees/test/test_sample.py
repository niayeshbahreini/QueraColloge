import unittest, math
from person import *
from worker import *
from teacher import *
from engineer import *

class ScoreListTest(unittest.TestCase):

    def test_a_scenario_for_worker(self):
        worker = Worker("amir", 18)
        self.assertEqual(worker.job, "worker", '\nدر تابع سازنده کلاس Worker، شغل فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(worker.level, 1, '\nدر تابع سازنده کلاس Worker، سطح فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(worker.name, "amir", '\nدر تابع سازنده کلاس Worker، نام فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(worker.age, 18, '\nدر تابع سازنده کلاس Worker، سن فرد را به درستی مقداردهی نمی‌کنید.')

        self.assertEqual(int(Consts.BASE_PRICE['worker'] * Consts.MIN_AGE / 18), worker.get_price(), '\nتابع get_price از کلاس Worker را به درستی پیاده‌سازی نکرده‌اید.')

        self.assertEqual(int(Consts.BASE_COST['worker'] / Consts.MIN_AGE * 18), worker.calc_life_cost(), '\nتابع calc_life_cost از کلاس Worker را به درستی پیاده‌سازی نکرده‌اید.')

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        worker.work_place = WorkPlace()
        worker.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['worker']['mine'] * Consts.MIN_AGE / 18), worker.calc_income(), '\nتابع calc_income از کلاس Worker را به درستی پیاده‌سازی نکرده‌اید.')

    def test_a_scenario_for_teacher(self):
        teacher = Teacher("niloo", 19)
        self.assertEqual(teacher.job, "teacher", '\nدر تابع سازنده کلاس Teacher، شغل فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(teacher.level, 1, '\nدر تابع سازنده کلاس Teacher، سطح فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(teacher.name, "niloo", '\nدر تابع سازنده کلاس Teacher، نام فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(teacher.age, 19, '\nدر تابع سازنده کلاس Teacher، سن فرد را به درستی مقداردهی نمی‌کنید.')

        self.assertEqual(int(Consts.BASE_PRICE['teacher'] - (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.get_price(), '\nتابع get_price از کلاس Teacher را به درستی پیاده‌سازی نکرده‌اید.')

        self.assertEqual(int(Consts.BASE_COST['teacher'] + (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.calc_life_cost(), '\nتابع calc_life_cost از کلاس Teacher را به درستی پیاده‌سازی نکرده‌اید.')

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        teacher.work_place = WorkPlace()
        teacher.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['teacher']['mine'] - (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.calc_income(), '\nتابع calc_income از کلاس Teacher را به درستی پیاده‌سازی نکرده‌اید.')

    def test_a_scenario_for_engineer(self):
        engineer = Engineer("yes! i'm an engineer", 37)
        self.assertEqual(engineer.job, "engineer", '\nدر تابع سازنده کلاس Engineer، شغل فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(engineer.level, 1, '\nدر تابع سازنده کلاس Engineer، سطح فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(engineer.name, "yes! i'm an engineer", '\nدر تابع سازنده کلاس Engineer، نام فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(engineer.age, 37, '\nدر تابع سازنده کلاس Engineer، سن فرد را به درستی مقداردهی نمی‌کنید.')

        self.assertEqual(int(Consts.BASE_PRICE['engineer'] * math.sqrt(Consts.MIN_AGE/37)), engineer.get_price(), '\nتابع get_price از کلاس Engineer را به درستی پیاده‌سازی نکرده‌اید.')

        self.assertEqual(int(Consts.BASE_COST['engineer'] * math.sqrt(37/Consts.MIN_AGE)), engineer.calc_life_cost(), '\nتابع calc_life_cost از کلاس Engineer را به درستی پیاده‌سازی نکرده‌اید.')

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        engineer.work_place = WorkPlace()
        engineer.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['engineer']['mine'] * math.sqrt(Consts.MIN_AGE/37)), engineer.calc_income(), '\nتابع calc_income از کلاس Engineer را به درستی پیاده‌سازی نکرده‌اید.')
