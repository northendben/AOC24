import re
import sys
sys.path.append("../")
import input_parser

input_data = input_parser.parse_input("str")
input_data = str(input_data).lower()

def part_one():
    regex = "mul\(\d{1,3},\d{1,3}\)"
    parsed_instructions = re.findall(regex,input_data)
    parsed_instructions = [row.replace("mul", "").replace("(", "").replace(")", "") for row in parsed_instructions]
    parsed_instructions = [row.split(",") for row in parsed_instructions]
    parsed_instructions = [[int(num) for num in row] for row in parsed_instructions]

    running_total = 0
    for row in parsed_instructions:
        value_to_add  = row[0] * row[1]
        running_total += value_to_add

    print(running_total)

def part_two():
    p2_regex = "(mul\(\d{1,3},\d{1,3}\)|don't|do)"
    parsed_instructions = re.findall(p2_regex,input_data)
    parsed_instructions = [row.replace("mul", "").replace("(", "").replace(")", "").replace('"',"").replace("'","") for row in parsed_instructions]
    parsed_instructions = [row.split(",") for row in parsed_instructions]
    parsed_instructions = [[int(num) if num[0] != "d" else num for num in row]for row in parsed_instructions]
    running_total = 0
    current_instruction = "do"
    for row in parsed_instructions:
        if type(row[0]) == str:
            current_instruction = row[0]
        else:
            if current_instruction == "do":
                value_to_add  = row[0] * row[1]
                running_total += value_to_add
    print(running_total)

part_one()
part_two()

