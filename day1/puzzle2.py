with open('input') as input:
    lines = input.readlines()

count = 0
previous_measurement = 0
sum = 0

for index, line in enumerate(lines):
    if index < 2:
        continue

    sum = int(line) + int(lines[index-1]) + int(lines[index-2])
    # print(f"{int(line)} + {int(lines[index-1])} + {int(lines[index-2])} = {sum}")

    if sum > previous_measurement:
        # print("increased")
        count += 1
    previous_measurement = sum

print(f"TOTAL: {count-1}")