with open('/home/steven/advent-of-code-2021/day5/input') as input:
    lines = input.readlines()

point_map = {}

for line in lines:
    line_split = line.strip('\n').replace('->', ',').split(',')
    x1 = int(line_split[0])
    y1 = int(line_split[1])
    x2 = int(line_split[2])
    y2 = int(line_split[3])

    if x1 > x2 and y1 > y2:
        tempX = x1
        tempY = y1
        while tempX >= x2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX - 1
            tempY = tempY - 1

    elif x1 > x2 and y2 > y1:
        tempX = x1
        tempY = y1
        while tempX >= x2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX - 1
            tempY = tempY + 1
    
    elif x2 > x1 and y1 > y2:
        tempX = x1
        tempY = y1
        while tempY >= y2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX + 1
            tempY = tempY - 1

    elif x2 > x1 and y2 > y1:
        tempX = x1
        tempY = y1
        while tempX <= x2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX + 1
            tempY = tempY + 1
    
    elif x1 == x2 and y1 > y2:
        tempX = x1
        tempY = y1
        while tempY >= y2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempY = tempY - 1

    elif x1 == x2 and y2 > y1:
        tempX = x1
        tempY = y1
        while tempY <= y2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempY = tempY + 1
    
    elif y1 == y2 and x2 > x1:
        tempX = x1
        tempY = y1
        while tempX <= x2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX + 1

    elif y1 == y2 and x1 > x2:
        tempX = x1
        tempY = y1
        while tempX >= x2:
            if f"{tempX},{tempY}" not in point_map.keys():
                point_map[f"{tempX},{tempY}"] = 1
            else:
                point_map[f"{tempX},{tempY}"] += 1
            tempX = tempX - 1

count = 0
for point in point_map.keys():
    if point_map[point] >= 2:
        count += 1

print(f"POINTS THAT OCCUR MORE THAN ONCE: {count}")