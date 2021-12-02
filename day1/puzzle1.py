with open('input') as input:
    lines = input.readlines()

count = 0
previous_measurement = 0

for line in lines:
    # print(int(line))

    if int(line) > previous_measurement:
        # print("increased")
        count += 1
    previous_measurement = int(line)
    
print(f"TOTAL: {count-1}")