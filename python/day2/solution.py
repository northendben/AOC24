import sys
import copy
sys.path.append('../')
import input_parser
input_data = input_parser.parse_input("num")
import pdb

unsafe_levels_list = []
def check_if_safe_p2(row, index):
    unsafe_levels = 0
    if index == 1:
        first_item_popped_row = copy.copy(row)
        first_item_popped_row.pop(index)
        second_item_popped_row = copy.copy(row)
        second_item_popped_row.pop(index - 1)
        levels_one, row = check_if_safe(first_item_popped_row)
        levels_two, row = check_if_safe(second_item_popped_row)
        unsafe_levels = levels_one + levels_two
    else:
        first_item_popped_row = copy.copy(row)
        first_item_popped_row.pop(index)
        second_item_popped_row = copy.copy(row)
        second_item_popped_row.pop(index + 1)
        levels_one, row = check_if_safe(first_item_popped_row)
        levels_two, row = check_if_safe(second_item_popped_row)
        unsafe_levels = levels_one + levels_two
    return unsafe_levels

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
            # new_row = copy.copy(row)
            # new_row.pop(index + 1)
            print(index)
            return unsafe_levels, index
    return unsafe_levels,index

def part_one():
    safe_rows = 0
    for row in input_data:
        unsafe_levels,index = check_if_safe(row)
        if unsafe_levels < 1:
            safe_rows += 1
    print(safe_rows)

def part_two():
    safe_rows = 0
    for x, row in enumerate(input_data):
        unsafe_levels,index = check_if_safe(row)
        if unsafe_levels < 1:
            safe_rows += 1
        elif unsafe_levels > 0:
            # pdb.set_trace()
            unsafe_levels = check_if_safe_p2(row, index)
            if unsafe_levels < 2:
                safe_rows += 1
            else:
                unsafe_levels_list.append(row)
    print(safe_rows)

part_one()
part_two()
import json
with open ('unsafelevels.json', 'w') as file:
    for row in unsafe_levels_list:
        file.write(json.dumps(row))
        file.write("\n")
