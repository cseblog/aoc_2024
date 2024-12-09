from unittest import TestCase

from day2 import part22


class Test(TestCase):
    def test_part2(self):
        int_arr = [70, 73, 72, 74, 74]

        self.assertEquals(True, part22(int_arr))

        int_arr = [3, 2, 5, 8, 9, 18]
