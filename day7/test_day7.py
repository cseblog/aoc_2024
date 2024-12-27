from unittest import TestCase
from day7 import Day7


class Test(TestCase):

    def test0(self):
        day7 = Day7("day7.input")
        print(day7.part_11())

    def test(self):
        day7 = Day7("day7.input")
        day7.process()
        print(day7.part_1(False))

    def test2(self):
        day7 = Day7("day7.sample2")
        day7.process()
        print(day7.part_1(False))

    def test_generate(self):
        day7 = Day7("day7.sample2")
        day7.process()

        mx = day7.generate_operator_maxtr(3)
        print(len(mx))

    def test_part_1(self):
        day7 = Day7("day7.input")
        day7.process()
        #2437272016585
        2437272016585
        print(day7.part_1(False))
