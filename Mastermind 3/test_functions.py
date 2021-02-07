import unittest
from io import StringIO
from unittest.mock import patch

import mastermind

class Test(unittest.TestCase):

    """
    Tests the code generated that is 4 digits and is between 1 to 8
    """
    def test_create_code(self):
        for i in range(100):
            code = mastermind.create_code()
            self.assertEqual(len(code), 4)
            for j in range(len(code)):
                self.assertTrue(1 <= code[j]  <= 8)

    """
    Checks if the digit is correct and returns true or false
    """               
    def test_check_correctness(self):
        turns = 12
        correct_digits_and_position = 0
        
        # correct = mastermind.check_correctness(turns)
        if correct_digits_and_position == 4:
            self.assertEqual(mastermind.check_correctness(turns, correct_digits_and_position), True)
        else:
            self.assertEqual(mastermind.check_correctness(turns, correct_digits_and_position), False)

    """
    Tests the answer input that it is 4 digits and between the range 1 to 8
    """
    @patch("sys.stdin", StringIO("12345\n5t678\n1234\n"))
    def test_answer_input(self):
        answer = mastermind.get_answer_input()
        self.assertEqual(len(answer), 4)
        for i in range(len(answer)):
            self.assertTrue(1 <= int(answer[i]) <= 8)

if __name__ == '__main__':
    unittest.main()
