from unittest import TestCase
from day4 import Day4

class Test(TestCase):
    def test_right_diagonal(sel):
        day4 = Day4("day4.test2")
        day4.process1()
        day4.get_right_diagonal()
        print(day4.right_diagonals)

    def test_left_diagonal(sel):
        day4 = Day4("day4.test2")
        day4.process1()
        day4.get_left_diagonal()
        print(day4.left_diagonals)

    def test_part1_1(self):
        day4 = Day4("day4.test")
        day4.process1()
        day4.get_cols()
        day4.get_right_diagonal()
        day4.get_left_diagonal()
        day4.find_part1()

    def test_part1_2(self):
        day4 = Day4("day4.txt")
        day4.process1()
        day4.get_cols()
        day4.get_right_diagonal()
        day4.get_left_diagonal()
        day4.find_part1()

    # Part 2
    def test_part2_1(self):
        day4 = Day4("day4.test3")
        day4.process1()
        day4.get_cols()
        day4.get_right_diagonal()
        day4.get_left_diagonal()
        day4.find_part2()

    def test_part2_2(self):
        day4 = Day4("day4.txt")
        day4.process1()
        day4.get_cols()
        day4.get_right_diagonal()
        day4.get_left_diagonal()
        day4.find_part2()
