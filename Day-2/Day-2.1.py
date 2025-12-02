import math

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

file_input = True

if file_input:
    with open("Day2.txt", "r", encoding="utf-8") as f:
        input = f.read()
else:
    input = example

def get_numbers():
    ranges = input.split(",")
    numbers = []

    for r in ranges:
        se = r.split("-")

        start = se[0]
        end = se[1]

        numbers = numbers + list(range(int(start),int(end) + 1))

    return list(set(numbers))

def check_validity(number: int):
    length = len(str(number))

    if length % 2 == 1:
        return True

    first_part = str(number)[:math.floor(length / 2)]
    second_part = str(number)[math.floor(length / 2):]

    return first_part != second_part

numbers = get_numbers()
sum = 0

for number in numbers:
    if not check_validity(number):
        sum += number

print(sum)