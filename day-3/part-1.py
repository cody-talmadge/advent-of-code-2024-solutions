import re
total = 0

def process_line(line):
    temp_total = 0
    matching_strings = re.findall(r'(mul\([0-9]+,[0-9]+\))', line)
    for string in matching_strings:
        numbers = re.findall(r'[0-9]+', string)
        temp_total += int(numbers[0]) * int(numbers[1])
    return temp_total

with open('input.txt') as file:
    for line in file:
        total += process_line(line)

print(total)