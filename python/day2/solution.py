import sys
import copy
sys.path.append('../')
import input_parser
input_data = input_parser.parse_input("num")
import pdb

def check_if_safe(row):
    unsafe_levels = 0
    for index, num in enumerate(row):
        if index == 0:
            if row[index + 1] > num:
                direction = "increasing"
            else:
                direction = "decreasing"
            if abs(num - row[index +1]) < 1 or abs(num-row[index+1]) > 3:
                unsafe_levels += 1
        elif index < len(row) - 1:
            if direction == "increasing":
                if row[index + 1] < num:
                    unsafe_levels += 1
            else:
                if row[index +1] > num:
                    unsafe_levels += 1
            if abs(num - row[index +1]) < 1 or abs(num-row[index+1]) > 3:
                unsafe_levels += 1
        if unsafe_levels > 0:
            new_row = copy.copy(row)
            new_row.pop(index + 1)
            return unsafe_levels, new_row
    return unsafe_levels, row

def part_one():
    safe_rows = 0
    for row in input_data:
        [unsafe_levels, new_row] = check_if_safe(row)
        if unsafe_levels < 1:
            safe_rows += 1
    print(safe_rows)

def part_two():
    safe_rows = 0
    for x, row in enumerate(input_data):
        unsafe_levels, new_row = check_if_safe(row)
        if unsafe_levels < 1:
            safe_rows += 1
        else:
            print(new_row)
            print(input_data[x] ,"SUP")
            unsafe_levels, new_row = check_if_safe(new_row)
            if unsafe_levels < 1:
                safe_rows += 1
    print(safe_rows)

part_one()
part_two()
