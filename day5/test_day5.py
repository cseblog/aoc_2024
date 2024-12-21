from unittest import TestCase
from day5 import Day5


class Test(TestCase):
    def test1(self):
        day5 = Day5("day5.sample")
        day5.process()
        print(day5.part1())

    def test2(self):
        day5 = Day5("day5.txt")
        day5.process()
        print(day5.part1())

    def test_part2(self):
        day5 = Day5("day5.sample")
        day5.process()
        print(day5.part2())

    def test_part2_2(self):
        day5 = Day5("day5.txt")
        day5.process()
        print(day5.part2())
