with open('input') as input:
    lines = input.readlines()

x_pos = 0
depth = 0
aim = 0

for line in lines:
    split_line = line.split()
    # print(split_line)
    instruction = split_line[0]
    value = int(split_line[1])

    if instruction == 'forward':
        x_pos += value
        depth += aim * value
    elif instruction == 'down':
        aim += value
    elif instruction == 'up':
        aim -= value
    
print(f"FINAL POSITION: X = {x_pos}, Y = {depth}\nANSWER = {x_pos * depth}")