import re
import sys
sys.path.append("../")
import input_parser
import pdb
import json
input_data = input_parser.parse_input("str")
locations = []
times_matched = 0
for index,row in enumerate(input_data):
    for inner_index, char in enumerate(row):
        if char.lower() == "x":
            locations.append((index, inner_index))

matches = []
def check_right(y_axis,x_axis):
    try:
        if input_data[y_axis][x_axis + 1] == "M" and input_data[y_axis][x_axis + 2] == "A" and input_data[y_axis][x_axis + 3] == "S":
            print("cr")
            return True
        else:
            return False
    except Exception as e:
        return False

def check_left(y_axis,x_axis):
    try:
        if input_data[y_axis][x_axis + -1] == "M" and input_data[y_axis][x_axis - 2] == "A" and input_data[y_axis][x_axis -3] == "S":
            print("cl")
            return True
        else:
            return False
    except Exception as e:
        return False
    
def check_up(y_axis,x_axis):
    try:
        if input_data[y_axis + 1][x_axis] == "M" and input_data[y_axis + 2][x_axis] == "A" and input_data[y_axis + 3][x_axis] == "S":
            print("cu")
            return True
        else:
            return False
    except Exception as e:
        return False
    
def check_down(y_axis,x_axis):
    try:
        if input_data[y_axis - 1][x_axis] == "M" and input_data[y_axis - 2][x_axis] == "A" and input_data[y_axis - 3][x_axis] == "S":
            print("cd")
            return True
        else:
            return False
    except Exception as e:
        return False
    
def check_ddr(y_axis,x_axis):
    try:
        if input_data[y_axis -1][x_axis +1] == "M" and input_data[y_axis - 2][x_axis +2] == "A" and input_data[y_axis -3][x_axis +3] == "S":
            print("ddr")
            return True
        else:
            return False
    except Exception as e:
        return False
def check_ddl(y_axis,x_axis):
    try:
        if input_data[y_axis -1][x_axis -1] == "M" and input_data[y_axis - 2][x_axis -2] == "A" and input_data[y_axis -3][x_axis -3] == "S":
            print('ddl')
            return True
        else:
            return False
    except Exception as e:
        return False
def check_udr(y_axis,x_axis):
    try:
        if input_data[y_axis +1 ][x_axis +1] == "M" and input_data[y_axis + 2][x_axis +2] == "A" and input_data[y_axis +3][x_axis +3] == "S":
            print('udr')
            return True
        else:
            return False
    except Exception as e:
        return False

def check_udl(y_axis,x_axis):
    try:
        if input_data[y_axis + 1][x_axis - 1] == "M" and input_data[y_axis + 2][x_axis - 2] == "A" and input_data[y_axis +3][x_axis -3] == "S":
            print('udl')
            return True
        else:
            return False
    except Exception as e:
        return False

for coordinate in locations:
    c_count = 0
    try:
        starting_y_axis = coordinate[0]
        starting_x_axis = coordinate[1]
        coordinate = tuple(map(str,coordinate))
        coordinate = ','.join(coordinate)
        dict_model = {
        coordinate: {
        "cr": False,
        "cl": False,
        "cd": False,
        "cu": False,
        "ddr": False,
        "ddl": False,
        "udl": False,
        "udr": False
    }
        }
 
        if check_right(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["cr"] = True
        if check_left(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["cl"] = True
        if check_down(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["cd"] = True
        if check_up(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["cu"] = True
        if check_ddr(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["ddr"] = True
        if check_ddl(starting_y_axis, starting_x_axis):
            c_count +=1
            dict_model[coordinate]["ddl"] = True
        if check_udl(starting_y_axis, starting_x_axis):
            c_count +=1 
            dict_model[coordinate]["udl"] = True
        if check_udr(starting_y_axis, starting_x_axis):
            c_count +=1
            dict_model[coordinate]["udr"] = True
        if c_count > 0:
            matches.append(dict_model)
        times_matched += c_count
    except Exception as E:
        print(E)

print(times_matched)
with open("day4_matches.json", "w") as file:
    file.write(json.dumps(matches, indent=2))
    file.close()
# top_barrier = 0
# bottom_barrier = len(input_data) - 1
# left_barrier = 0
# right_barrier = len(input_data[0]) - 1

# def check_for_letters(letter_to_find, y_axis, x_axis):
#     # pdb.set_trace()
#     if x_axis > left_barrier:
#         left_range = -1
#     else:
#         left_range = 0
#     if x_axis < right_barrier:
#         right_range = 2
#     else:
#         right_range = 1

#     if y_axis > top_barrier:
#         for num in range(left_range,right_range):
#             if input_data[y_axis - 1][x_axis + num] == letter_to_find:
#                 return [True, (y_axis - 1,x_axis+num)]
            
#     if y_axis < bottom_barrier:
#          for num in range(left_range,right_range):
#             if input_data[y_axis + 1][x_axis + num] == letter_to_find:
#                 return [True, (y_axis + 1, x_axis + num)]
            
#     for num in range(left_range,right_range):
#         if input_data[y_axis][x_axis + num] == letter_to_find:
#             return [True, (y_axis, x_axis +num)]
#     return [False, (500,500)]

# for coordinate in locations:
#     loc = []
#     starting_y_axis = coordinate[0]
#     starting_x_axis = coordinate[1]
#     loc.append((starting_y_axis, starting_x_axis))
#     found_m, c = check_for_letters("M", starting_y_axis, starting_x_axis)
#     if found_m:
#         loc.append(c)
#         found_a, c = check_for_letters("A", c[0], c[1])
#         if found_a:
#             loc.append(c)
#             found_s,c = check_for_letters("S", c[0], c[1])
#             if found_s:
#                 loc.append(c)
#     if found_m and found_a and found_s:
#         times_matched += 1
#         print(loc)
# print(times_matched)
        


    

    

