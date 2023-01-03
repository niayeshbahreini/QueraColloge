import unittest
from function import comb


class FunctionTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_return_value(self):
        self.assertTrue(comb(1, 1) is not None, "باید مقدار محاسبه شده رو return کنی.")
        self.assertTrue((type(comb(1, 1)) is int) or (type(comb(1, 1)) is float),
                        "جنس خروجی تابع باید از نوع int یا همان عدد باشد.")

    def test_sample_normal(self):
        self.assertEqual(3, comb(3, 2), 'خروجی تابع برای comb(3, 2) باید برابر ۳ باشد.')

    def test_sample_k_is_equal_to_zero(self):
        self.assertEqual(1, comb(3, 0), 'خروجی تابع برای comb(3, 0) باید برابر ۱ باشد.')

    def test_k_is_greater_than_n(self):
        self.assertEqual(0, comb(3, 4), 'خروجی تابع برای comb(3, 4) باید برابر ۰ باشد.')
