from unittest import TestCase
from day6 import Day6


class Test(TestCase):
    def test(self):
        day6 = Day6("day6.sample2")
        day6.process()
        print(day6.actor.to_string())
        print(day6.part_1(True))

    def test_part_1(self):
        day6 = Day6("day6.input")
        day6.process()
        # print(day6.actor.to_string())
        print(day6.part_1(False))

    def test_part_2_1(self):
        day6 = Day6("day6.sample2")
        day6.process()
        print(day6.part_2(False))

    def test_part_2(self):
        day6 = Day6("day6.input")
        day6.process()
        print(day6.part_2(False))
