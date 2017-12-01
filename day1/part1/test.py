import unittest

from hamcrest import *
from day1.part1 import main


class MainTest(unittest.TestCase):

    def test_first_example(self):
        assert_that(main.run('1122'), equal_to(3))

    def test_second_example(self):
        assert_that(main.run('1111'), equal_to(4))

    def test_third_example(self):
        assert_that(main.run('1234'), equal_to(0))

    def test_fourth_example(self):
        assert_that(main.run('91212129'), equal_to(9))
