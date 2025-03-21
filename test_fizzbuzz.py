import unittest
from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(fizz_buzz(15)[14], "FizzBuzz")  # 15th element

    def test_fizzbuzz_divisible_by_3(self):
        self.assertEqual(fizz_buzz(3)[2], "Fizz")  # 3rd element

    def test_fizzbuzz_divisible_by_5(self):
        self.assertEqual(fizz_buzz(5)[4], "Buzz")  # 5th element

    def test_fizzbuzz_not_divisible_by_3_or_5(self):
        self.assertEqual(fizz_buzz(2), ["1", "2"])  # First two elements

    def test_fizzbuzz_edge_case_n_1(self):
        self.assertEqual(fizz_buzz(1), ["1"])  # Single element

    def test_fizzbuzz_edge_case_n_0(self):
        self.assertEqual(fizz_buzz(0), [])  # Empty list

if __name__ == "__main__":
    unittest.main()