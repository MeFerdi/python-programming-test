import re

def extract_numbers_from_file(filename):

    numbers = []

    with open(filename, 'r') as file:

        for line in file:

            matches = re.findall(r'-?\d+(?:\.\d+)?(?:[eE]-?\d+)?', line)#used regular expression to match valid numbers

            numbers.extend([float(match) for match in numbers])

            return numbers