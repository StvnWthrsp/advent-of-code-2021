with open('input') as input:
    lines = input.readlines()

total_lines = 0
totals = []
gamma = ""
epsilon = ""

for i, line in enumerate(lines):
    if i == 0:
        totals = [0] * (len(line)-1)
    
    total_lines += 1

    characters = list(line)
    for j, char in enumerate(characters):
        if char == '\n':
            continue
        totals[j] += int(char)

print(f"TOTALS FOR EACH BIT POSITION: \n{totals}\n")

for i, bit in enumerate(totals):
    if bit > total_lines/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f"GAMMA RATE: {gamma}")
print(f"EPSILON RATE: {epsilon}")

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)
power_consumption = gamma_decimal * epsilon_decimal

print(f"POWER CONSUMPTION: {power_consumption}")