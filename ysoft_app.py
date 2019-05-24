import sys
import os
import json
import string


def parse_arguments():
    print(sys.argv)

    if len(sys.argv) != 5:
        print("Provide 4 arguments in this order:\n"
              "name of user, name of printer, path to input text file, path to output JSON file. ")
        sys.exit()

    user, printer, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    if not user or not printer:
        print("Provide non-empty names for user and printer")
        sys.exit()

    if not (os.path.isfile(input_file) and
            os.path.isfile(output_file) and
            os.path.split(output_file)[1].lower().endswith('.json')):
        print("Provide valid files")
        sys.exit()

    parse_data_from_file(user, printer, input_file, output_file)


def write_JSON_file(user, printer, output_file, data):
    with open(output_file, 'w') as JSON_file:
        json_dict = {'userName': user, 'printerName': printer, 'data': data}
        json.dump(json_dict, JSON_file, ensure_ascii=False, indent=2)


def print_lower_ascii(data):
    for letter in string.ascii_lowercase:
        letter_count = data.count(letter)
        if letter_count > 0:
            print("{}:{}".format(letter, letter_count))


def parse_data_from_file(user, printer, input_file, output_file):
    with open(input_file) as file:
        data = file.read()
        write_JSON_file(user, printer, output_file, data)
        print_lower_ascii(data)


parse_arguments()
