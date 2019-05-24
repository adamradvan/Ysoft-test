import unittest
from ysoft_app import get_lower_ascii_data
from ysoft_app import parse_arguments
from ysoft_app import parse_data_from_file
from ysoft_app import write_json_file


class TestGetLowerAsciiData(unittest.TestCase):
    def test_simple(self):
        data = "d aa b c aa"
        expected = "a: 4\n" \
                   "b: 1\n" \
                   "c: 1\n" \
                   "d: 1\n"
        self.assertEqual(get_lower_ascii_data(data), expected)

    def test_advanced(self):
        data = "9Ac%5d _uUU3%uUU5u$!@#@!Dc"
        expected = "c: 2\n" \
                   "d: 1\n" \
                   "u: 3\n"
        self.assertEqual(get_lower_ascii_data(data), expected)

    def test_empty(self):
        data = ""
        expected = ""
        self.assertEqual(get_lower_ascii_data(data), expected)

    def test_no_lowercase(self):
        data = "A^9B51\nC_ "
        expected = ""
        self.assertEqual(get_lower_ascii_data(data), expected)

