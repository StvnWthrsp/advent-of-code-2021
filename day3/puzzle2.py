with open('input') as input:
    lines = input.readlines()

def getMostFrequentBit(index, lines):
    zero_bits = 0
    one_bits = 0
    for line in lines:
        if line[index] == '0':
            zero_bits += 1
        else:
            one_bits += 1
    if zero_bits > one_bits:
        greater = 0
    else:
        greater = 1
    return greater

def getLeastFrequentBit(index, lines):
    zero_bits = 0
    one_bits = 0
    for line in lines:
        if line[index] == '0':
            zero_bits += 1
        else:
            one_bits += 1
    if zero_bits > one_bits:
        lesser = 1
    else:
        lesser = 0
    return lesser

def removeInvalidNumbers(frequent_bit, index, lines):
    lines_copy = list(lines)
    for line in lines:
        if int(line[index]) != frequent_bit:
            lines_copy.remove(line)
    return lines_copy

def recursivelyGetOxygenGeneratorRating(index, lines):
    bit = getMostFrequentBit(index, lines)
    remaining_lines = removeInvalidNumbers(bit, index, lines)
    # print(remaining_lines)
    if len(remaining_lines) == 1:
        return remaining_lines
    else:
        return recursivelyGetOxygenGeneratorRating(index+1, remaining_lines)

def recursivelyGetCO2ScrubberRating(index, lines):
    bit = getLeastFrequentBit(index, lines)
    remaining_lines = removeInvalidNumbers(bit, index, lines)
    # print(remaining_lines)
    if len(remaining_lines) == 1:
        return remaining_lines
    else:
        return recursivelyGetCO2ScrubberRating(index+1, remaining_lines)

oxygen_generator_binary = recursivelyGetOxygenGeneratorRating(0, lines)
co2_generator_binary = recursivelyGetCO2ScrubberRating(0, lines)

oxygen_generator_binary = oxygen_generator_binary[0].strip('\n')
co2_generator_binary = co2_generator_binary[0].strip('\n')

oxygen_generator_decimal = int(oxygen_generator_binary, 2)
co2_generator_decimal = int(co2_generator_binary, 2)

solution = oxygen_generator_decimal*co2_generator_decimal

print(solution)