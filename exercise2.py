import re

def find_single_valid_number(line):
    
    match = re.match(r"^\s*([-+]?\d*\.\d+|[-+]?\d+)\s*$", line)
    
    if match:
        return float(match.group(1))
    else:
        return None

def extract_numbers_from_file(filename):
    numbers = []

    with open(filename, 'r') as file:
        for line in file:
        
            number = find_single_valid_number(line)
            
            # Add the valid number to the list
            if number is not None:
                numbers.append(number)

    return numbers
