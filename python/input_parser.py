def parse_input(type):
    input_data = []
    if type == "str":
        with open("input.txt", "r") as file:
            for row in file:
                input_data.append(row)
        return input_data
    else: 
        with open("input.txt", "r") as file:
            for row in file:
                input_data.append([int(num) for num in row.split()])
        return input_data
    