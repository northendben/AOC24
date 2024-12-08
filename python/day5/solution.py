def part_one():
    rules = {}
    updates = []
    match_tally = 0 
    with open("input.txt", "r") as file:
        finding_rules = True
        for row in file:
            row = row.replace("\n", "")
            if len(row) < 2:
                finding_rules = False
            if finding_rules:
                holding_row = row.split("|")
                key = int(holding_row[0])
                if key in rules.keys():
                    rules[key].append(int(holding_row[1]))
                else: 
                    rules[key] = [int(holding_row[1])]
            elif not finding_rules and row != "":
                updates.append([int(num) for num in row.split(",")])
    for row in updates:
        all_match = True
        length = len(row)
        for index, num in enumerate(row):
            for cnum in range(index + 1, length):
                if index < length -1:
                    if num in rules.keys():
                        if not row[cnum] in rules[num]:
                            all_match = False
                    else:
                        all_match = False
        if all_match:
            middle_index = int(length/2 -.5)
            match_tally += row[middle_index]
    print(match_tally)

def part_two():
    all_fine = []
    match_tally = 0 
    rules = {}
    updates = []
    match_tally = 0 
    with open("input.txt", "r") as file:
        finding_rules = True
        for row in file:
            row = row.replace("\n", "")
            if len(row) < 2:
                finding_rules = False
            if finding_rules:
                holding_row = row.split("|")
                key = int(holding_row[0])
                if key in rules.keys():
                    rules[key].append(int(holding_row[1]))
                else: 
                    rules[key] = [int(holding_row[1])]
            elif not finding_rules and row != "":
                updates.append([int(num) for num in row.split(",")])
    for arr in updates:
        should_count = False
        for n in range(len(arr)):
            swapped = False  
            for i in range(len(arr)-1):
                if arr[i] in rules.keys():
                    if arr[i+1] not in rules[arr[i]]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                        should_count = True
                else:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    should_count = True
            if not swapped and should_count:
                middle_index = int(len(arr)/2 -.5)
                match_tally += int(arr[middle_index])
                break
            elif not swapped:
                break
    print(match_tally)               


part_one()
part_two()