import unittest

from hamcrest import *
from day1.part2 import main


class MainTest(unittest.TestCase):

    def test_first_example(self):
        assert_that(main.run('1212'), equal_to(6))

    def test_second_example(self):
        assert_that(main.run('1221'), equal_to(0))

    def test_third_example(self):
        assert_that(main.run('123425'), equal_to(4))

    def test_fourth_example(self):
        assert_that(main.run('123123'), equal_to(12))

    def test_fifth_example(self):
        assert_that(main.run('12131415'), equal_to(4))
