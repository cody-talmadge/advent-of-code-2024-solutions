left_numbers = []
right_numbers = []
total_difference = 0

with open('input.txt') as file:
    for line in file:
        left, right = line.split('   ')
        left_numbers.append(int(left))
        right_numbers.append(int(right))

left_numbers.sort()
right_numbers.sort()

for i in range(len(left_numbers)):
        left = left_numbers[i]
        right = right_numbers[i]
        difference = abs(int(left) - int(right))
        total_difference += difference

print(total_difference)