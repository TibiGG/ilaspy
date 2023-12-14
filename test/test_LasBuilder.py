from unittest import TestCase

from ilaspy.LasBuilder import LasBuilder


class TestLasBuilder(TestCase):
    def test_add_one_explicit_hypothesis(self):
        las = LasBuilder()
        las.add_explicit_hypothesis(1, "p")
        self.assertEqual("1 ~ p.", las.to_string())

    def test_add_two_explicit_hypothesis(self):
        las = LasBuilder()
        las.add_explicit_hypothesis(1, "p")
        las.add_explicit_hypothesis(2, "p :- r")
        expected_las = ("1 ~ p.\n"
                        "2 ~ p :- r.")
        self.assertEqual(expected_las, las.to_string())

    def test_add_all_explicit_hypothesis(self):
        las = LasBuilder()
        las.add_explicit_hypothesis(1, "p")
        las.add_explicit_hypothesis(2, "p :- r")
        las.add_explicit_hypothesis(2, "p :- not s")
        las.add_explicit_hypothesis(3, "p :- r, not s")
        expected_las = ("1 ~ p.\n"
                        "2 ~ p :- not s.\n"
                        "2 ~ p :- r.\n"
                        "3 ~ p :- r, not s.")
        self.assertEqual(expected_las, las.to_string())

    def test_add_in_order_explicit_hypothesis(self):
        las = LasBuilder()
        las.add_explicit_hypothesis(2, "p :- r")
        las.add_explicit_hypothesis(3, "p :- r, not s")
        las.add_explicit_hypothesis(2, "p :- not s")
        las.add_explicit_hypothesis(1, "p")
        expected_las = ("1 ~ p.\n"
                        "2 ~ p :- not s.\n"
                        "2 ~ p :- r.\n"
                        "3 ~ p :- r, not s.")
        self.assertEqual(expected_las, las.to_string())

    def test_add_mode_bias(self):
        assert False
