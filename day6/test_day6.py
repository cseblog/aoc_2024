from unittest import TestCase
from day6 import Day6


class Test(TestCase):
    def test(self):
        day6 = Day6("day6.sample")
        day6.process()
        print(day6.actor.to_string())
        print(day6.part_1())

    def test_part_1(self):
        day6 = Day6("day6.input")
        day6.process()
        # print(day6.actor.to_string())
        print(day6.part_1())

