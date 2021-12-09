with open('/home/steven/advent-of-code-2021/day5/input') as input:
    lines = input.readlines()

point_map = {}

first_vent = lines[0]
line_split = first_vent.strip('\n').replace('->', ',').split(',')
x1 = int(line_split[0])
y1 = int(line_split[1])
x2 = int(line_split[2])
y2 = int(line_split[3])

for line in lines:
    line_split = line.strip('\n').replace('->', ',').split(',')
    x1 = int(line_split[0])
    y1 = int(line_split[1])
    x2 = int(line_split[2])
    y2 = int(line_split[3])

    if x1 == x2 or y1 == y2:
        if x1 == x2 and y1 > y2:
            y1, y2 = y2, y1
        if y1 == y2 and x1 > x2:
            x1, x2 = x2, x1
        # print(f"{x1},{y1}->{x2},{y2}")
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                # print(f"{x},{y}")
                if f"{x},{y}" not in point_map.keys():
                    point_map[f"{x},{y}"] = 1
                else:
                    point_map[f"{x},{y}"] += 1

count = 0
for point in point_map.keys():
    if point_map[point] >= 2:
        count += 1

print(f"POINTS THAT OCCUR MORE THAN ONCE: {count}")