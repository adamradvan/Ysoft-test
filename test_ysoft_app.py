import unittest
import json
from ysoft_app import get_lower_ascii_data
from ysoft_app import validate_arguments
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


class TestValidateArguments(unittest.TestCase):
    def setUp(self):
        self.user = "test UserName"
        self.printer = "test PrinterName"
        self.input_file = "test_input.txt"
        self.output_file = "test_output.json"

    def test_ok_arguments(self):
        try:
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)
        except SystemExit:
            self.fail("Function validate_arguments() failed despite providing correct arguments")

    def test_nok_output_file_not_JSON(self):
        with self.assertRaises(SystemExit):
            self.output_file = "test_output.txt"
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)

    def test_nok_user_name_empty(self):
        with self.assertRaises(SystemExit):
            self.user = ""
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)

    def test_nok_printer_name_empty(self):
        with self.assertRaises(SystemExit):
            self.printer = ""
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)

    def test_nok_invalid_input_path(self):
        with self.assertRaises(SystemExit):
            self.input_file = "C:"
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)

    def test_nok_invalid_output_path(self):
        with self.assertRaises(SystemExit):
            self.output_file = "C:"
            validate_arguments(self.user, self.printer, self.input_file, self.output_file)


class TestWriteJSONFile(unittest.TestCase):
    def setUp(self):
        self.user = "test UserName"
        self.printer = "test PrinterName"
        self.output_file = "test_output.json"
        self.data = "This is test data."

    def test_write_json_file(self):
        write_json_file(self.user, self.printer, self.output_file, self.data)
        with open(self.output_file) as f:
            json_from_file = json.load(f)
            self.assertEqual(self.user, json_from_file['userName'])
            self.assertEqual(self.printer, json_from_file['printerName'])
            self.assertEqual(self.data, json_from_file['data'])

    def test_write_json_file_empty_data(self):
        self.data = ""
        write_json_file(self.user, self.printer, self.output_file, self.data)
        with open(self.output_file) as f:
            json_from_file = json.load(f)
            self.assertIn('userName', json_from_file)
            self.assertIn('printerName', json_from_file)
            self.assertIn('data', json_from_file)
            self.assertEqual(self.user, json_from_file['userName'])
            self.assertEqual(self.printer, json_from_file['printerName'])
            self.assertEqual(self.data, json_from_file['data'])
