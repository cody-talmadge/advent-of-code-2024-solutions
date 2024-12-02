safe_count = 0

def check_numbers(numbers):
    incrementing = numbers[1] > numbers[0]

    min_diff = 1 if incrementing else -3
    max_diff = 3 if incrementing else -1

    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff > max_diff or diff < min_diff:
            return False

    return True

with open('input.txt') as file:
    for line in file:
        numbers = line.split(' ')
        numbers = [int(number) for number in numbers]
        if check_numbers(numbers):
            safe_count += 1

print(safe_count)