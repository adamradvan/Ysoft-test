import sys
import os
import json
import string


def parse_arguments():
    if len(sys.argv) != 5:
        print("Provide 4 arguments in this order:\n"
              "[name of user], [name of printer], [path to input text file], [path to output JSON file]")
        sys.exit()

    user, printer, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    validate_arguments(user, printer, input_file, output_file)
    parse_data_from_file(user, printer, input_file, output_file)


def validate_arguments(user, printer, input_file, output_file):
    if not user or not printer:
        print("Provide non-empty names for user and printer")
        sys.exit()

    if not (os.path.isfile(input_file)):
        print("Provide valid valid path to input file")
        sys.exit()

    if not os.path.split(output_file)[1].lower().endswith('.json'):
        print("Provide valid path to .json file")
        sys.exit()


def parse_data_from_file(user, printer, input_file, output_file):
    try:
        with open(input_file) as file:
            data = file.read()
            write_json_file(user, printer, output_file, data)
            print(get_lower_ascii_data(data))
    except PermissionError:
        print("Insufficient access right for file {}".format(input_file))
        sys.exit()
    except OSError as err:
        print("I/O failure: {}".format(err))
        sys.exit()


def write_json_file(user, printer, output_file, data):
    try:
        with open(output_file, 'w') as JSON_file:
            json_dict = {'userName': user, 'printerName': printer, 'data': data}
            json.dump(json_dict, JSON_file, ensure_ascii=False, indent=2)
    except PermissionError:
        print("Insufficient access right for file {}".format(output_file))
        sys.exit()


def get_lower_ascii_data(data):
    output = ""
    for letter in string.ascii_lowercase:
        letter_count = data.count(letter)
        if letter_count > 0:
            output += ("{}: {}\n".format(letter, letter_count))
    return output


if __name__ == '__main__':
    parse_arguments()
