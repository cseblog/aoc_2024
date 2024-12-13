from unittest import TestCase

from day4 import Day4


class Test(TestCase):
    def test_part2(self):
        day4 = Day4("day4.test")
        day4.process1()
        day4.find_word_1()

    # Purely matrix travel
