safe_count = 0

input = []
with open('input.txt') as file:
    for line in file:
        numbers = line.split(' ')
        numbers = [int(number) for number in numbers]
        if numbers[1] > numbers[0]:
            incrementing = True
        else:
            incrementing = False

        safe = 1
        if incrementing:
            for i in range(len(numbers) - 1):
                diff = numbers[i + 1] - numbers[i]
                print(numbers, diff)
                if diff > 3:
                    safe = 0
                if diff < 1:
                    safe = 0
        else:
            for i in range(len(numbers) - 1):
                diff = numbers[i] - numbers[i + 1]
                if diff > 3:
                    safe = 0
                if diff < 1:
                    safe = 0
        print(safe)
        safe_count += safe

print(safe_count)