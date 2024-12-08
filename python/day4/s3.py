def parse(data):
    total_xmas = 0
    up = {"row":[-1, -2, -3]}
    down = {"row":[1, 2, 3]}
    left = {"col":[-1, -2, -3]}
    right = {"col":[1, 2, 3]}
    up_left = {"row":[-1, -2, -3], "col":[-1, -2, -3]}
    up_right = {"row":[-1, -2, -3], "col":[1, 2, 3]}
    down_left = {"row":[1, 2, 3], "col":[-1, -2, -3]}
    down_right = {"row":[1, 2, 3], "col":[1, 2, 3]}
    for i in data.keys():
        count = 0
        for n in data[i]:
            if n == 'X':
                # print(n)
                if i > 3:
                    if search(data, i, count, up):
                        total_xmas += 1
                    if count > 2:
                        if search(data, i, count, up_left):
                            total_xmas += 1
                    if count < 138:
                        if search(data, i, count, up_right):
                            total_xmas += 1
                if i < 138:
                    if search(data, i, count, down):
                        total_xmas += 1
                    if count > 2:
                        if search(data, i, count, down_left):
                            total_xmas += 1
                    if count < 138:
                        if search(data, i, count, down_right):
                            total_xmas += 1
                if count > 2:
                    if search(data, i, count, left):
                        total_xmas += 1
                if count < 138:
                    if search(data, i, count, right):
                        total_xmas += 1
            count += 1
    return total_xmas

def search(frame, index, column, direction):
    # print("searching")
    if "row" in direction.keys():
        if "col" in direction.keys():
            if frame[(index+direction["row"][0])][(column+direction["col"][0])] == "M":
                print("index:{0}, column:{1}, fi: {2}, fc: {3}".format(
                    index,
                    column,
                    (index + direction["row"][0]),
                    (column+direction["col"][0])
                ))
                # print(frame[(index+direction["row"][0])][(column+direction["col"][0])])
                if frame[(index + direction["row"][1])][(column + direction["col"][1])] == "A":
                    # print(frame[(index + direction["row"][1])][(column + direction["col"][1])])
                    if frame[(index + direction["row"][2])][(column + direction["col"][2])] == "S":
                        # print(frame[(index + direction["row"][2])][(column + direction["col"][2])])
                        print("Found diaganol")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            if frame[(index+direction["row"][0])][column] == "M":
                # print(frame[(index+direction["row"][0])][column])
                if frame[(index + direction["row"][1])][column] == "A":
                    # print(frame[(index + direction["row"][1])][column])
                    if frame[(index + direction["row"][2])][column] == "S":
                        # print(frame[(index + direction["row"][2])][column])
                        # print("found vertical")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        if frame[index][(column+direction["col"][0])] == "M":
            # print(frame[index][(column+direction["col"][0])])
            if frame[index][(column+direction["col"][1])] == "A":
                # print(frame[index][(column+direction["col"][1])])
                if frame[index][(column + direction["col"][2])] == "S":
                    # print(frame[index][(column + direction["col"][2])])
                    # print("found horizontal")
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False






in_file = open("input.txt")
count = 1
grid = {}
for x in in_file:
    grid[count] = x
    count += 1
total = parse(grid)
print(total)