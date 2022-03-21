import os
import sys
import unittest
from test.tests import TEST_CASES

from blossom import get_page_content

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class GoodsTestCase(unittest.TestCase):

    def setUp(self):
        """Начальные условия для тестов."""
        self.test_cases = TEST_CASES

    def test_data_for_query(self):
        """Тесирование функции."""
        for test_case in self.test_cases:
            test_inp = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertEqual(expected, get_page_content(test_inp)['get_page_content']['is_success'])
