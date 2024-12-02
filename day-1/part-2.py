left_numbers = []
right_numbers = []
right_number_count = dict()
similarity_score = 0

with open('input.txt') as file:
    for line in file:
        left, right = line.split('   ')
        left_numbers.append(int(left))
        right_numbers.append(int(right))

for num in right_numbers:
    if num not in right_number_count:
        right_number_count[num] = 1
    else:
        right_number_count[num] += 1

for num in left_numbers:
    if num in right_number_count:
        similarity_score += num * right_number_count[num]

print(similarity_score)