import unittest
from function import day_calculator


class FunctionTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_return_value(self):
        self.assertTrue(day_calculator('1999-10-13') is not None, "باید مقدار محاسبه شده رو return کنی.")
        self.assertTrue((type(day_calculator('1999-10-13')) is int) or (type(day_calculator('1999-10-13')) is str),
                        "جنس خروجی تابع باید از نوع int یا str باشد.")

    def test_sample_one_month_old(self):
        self.assertEqual(30, day_calculator('1999-2-13'), 'در تاریخ 13-2-1999، سجاد ۳۰ روز زندگی کرده است.')

    def test_sample_not_yet_born(self):
        self.assertEqual('Not yet born', day_calculator('1999-01-13'),
                         'در تاریخ 13-01-1999، سجاد هنوز بدنیا نیامده است.')
