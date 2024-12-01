import string
import re
left_side = []
right_side = []
differences = []
with open('input.txt', 'r') as file:
    for row in file:
        row = re.sub(" +", ",", row)
        row = row.replace("\n", "")
        split_row = row.split(',')
        print(split_row)
        left_side.append(int(split_row[0]))
        right_side.append(int(split_row[1]))

left_side.sort()
right_side.sort()

for num in range(0,len(left_side)):
    difference = abs(left_side[num] - right_side[num])
    differences.append(difference)

print(sum(differences))