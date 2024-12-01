import string
import re
left_side = []
right_side = []
part_one_difference = 0
part_two_similarity = 0
java_file = ""
with open('input.txt', 'r') as file:
    for row in file:
        row = re.sub(" +", ",", row)
        java_file += row
        row = row.replace("\n", "")
        split_row = row.split(',')
        print(split_row)
        left_side.append(int(split_row[0]))
        right_side.append(int(split_row[1]))
    with open("../../java/day1/input.txt", 'w') as file2:
        file2.write(java_file)

left_side.sort()
right_side.sort()

def part_one(part_one_difference):
    for num in range(0,len(left_side)):
        difference = abs(left_side[num] - right_side[num])
        part_one_difference += difference
    
    print(part_one_difference)

def part_two(part_two_similarity):
    for num in left_side:
        num_of_occurences = right_side.count(num)
        score = num_of_occurences * num
        part_two_similarity += score
    print(part_two_similarity)

part_one(part_one_difference)
part_two(part_two_similarity)