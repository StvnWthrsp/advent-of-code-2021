with open('/home/steven/advent-of-code-2021/day7/input') as input:
    lines = input.readlines()
positions = lines[0].split(',')
positions = [int(i) for i in positions]
max_pos = max(positions)
fuel_sums = {}
for i in range(0, max_pos+1):
    fuel_sum = 0
    for pos in positions:
        fuel = abs(i - pos)
        fuel_sum += fuel
    fuel_sums[i] = fuel_sum

minimum_fuel = min(fuel_sums.values())
for i, fuel_val in enumerate(fuel_sums.values()):
    if fuel_val == minimum_fuel:
        print(f"OPTIMAL POSITION: {i}")
print(f"FUEL REQUIRED = {minimum_fuel}")