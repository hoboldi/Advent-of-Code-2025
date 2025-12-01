example = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

file_input = True

if file_input:
    with open("Day1.txt", "r", encoding="utf-8") as f:
        input = f.read()
else:
    input = example

commands = input.split("\n")

count = 50
zeros = 0

for command in commands:
    direction = command[0]
    number = int(command[1:])

    if direction == "L":
        count = (count - number) % 100

    if direction == "R":
        count = (count + number) % 100

    if count == 0:
        zeros += 1

print(zeros)