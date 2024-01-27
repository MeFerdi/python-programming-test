import re

def find_single_valid_number(line):
      match = re.match(r"^\s*([-+]?\d+\.?\d*(?:[eE][-+]?\d+)?)\s*$", line)
    if match:
        number = match.group(1)
        return int(number) if '.' not in number and 'e' not in number.lower() else float(number)
    else:
        return None

def extract_numbers_from_file(filename):
    numbers = []

    with open(filename, 'r') as file:
        for line in file:
            number = find_single_valid_number(line)
            
            # Adding the valid number to the list
            if number is not None:
                numbers.append(number)

    return numbers
