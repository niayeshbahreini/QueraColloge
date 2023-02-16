import unittest
from solution import solve


class ScoreListTest(unittest.TestCase):
    def _write_to_file(self, path, data):
        with open(path, 'w') as f:
            f.write(data)

    def test_1(self):
        code = "a = input()\n\nb = int(a)\nprint(b * b, a + a)\n#if a = 3 output is 33."

        self._write_to_file("in.py", code)
        self.assertEqual(solve("in.py"), 3, '\nخروجی تابع برای ورودی\na = input()\n\nb = int(a)\nprint(b * b, a + a)\n#if a = 3 output is 33.\nبرابر ۳ است.')

    def test2(self):
        code = "a= input()\n\n###\n#a = input()\nprint(a)"

        self._write_to_file("in.py", code)
        self.assertEqual(solve("in.py"), 2, '\nخروجی تابع برای ورودی\na= input()\n\n###\n#a = input()\nprint(a)\nبرابر ۲ است.')