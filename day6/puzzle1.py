with open('/home/steven/advent-of-code-2021/day6/input') as input:
    lines = input.readlines()

# Create a map to hold the total number of fish with each timer value
fish_map = {}
for num in lines[0].split(','):
    if int(num) not in fish_map.keys():
        fish_map[int(num)] = 1
    else:
        fish_map[int(num)] += 1

for i in range(1, 257):
    new_map = {}

    for j in range(0, 9):

        # Fill value of 0 for missing keys to prevent invalid key values in first iteration
        if j not in fish_map.keys():
            fish_map[j] = 0

        # Set total number of fish with timers at 6 and 8 equal to the number previously at 0
        if j == 0:
            new_map[8] = fish_map[0]
            new_map[6] = fish_map[0]

        # Account for the logic above for number of fish with timers at 6
        elif j == 7:
            new_map[6] += fish_map[7]

        # Total number of fish with timer at j-1 is set equal to number of fish with timer at j
        else:
            new_map[j-1] = fish_map[j]
    
    fish_map = new_map
sum = 0
for val in fish_map.values():
    sum += val
print(f"TOTAL NUMBER OF LANTERNFISH: {sum}")