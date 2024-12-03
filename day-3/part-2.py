import re
total = 0
adding = True

def process_line(line):
    global adding
    temp_total = 0
    matching_strings = re.findall(r'(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))', line)
    for string in matching_strings:
        if string[1] == 'do()':
            adding = True
        elif string[2] == 'don\'t()':
            adding = False
        else:
            if adding:
                numbers = re.findall(r'[0-9]+', string[0])
                temp_total += int(numbers[0]) * int(numbers[1])
    return temp_total

with open('input.txt') as file:
    for line in file:
        total += process_line(line)

print(total)