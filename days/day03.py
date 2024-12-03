data = load_data("day03")

line = 0
end = len(data)

inscope = False
current = []
numbers = []
previous_number = []
current_number = []
enabled = True

for i in range(end):
    if line >= end:
        break

    if data[line : line + 4] == "do()":
        enabled = True
        line += 4
        continue

    if data[line : line + 7] == "don't()":
        enabled = False
        line += 7
        continue

    if not inscope and data[line] == "m":
        inscope = True
        current.append(data[line])
        line += 1
    elif inscope and current == ["m"] and data[line] == "u":
        current.append(data[line])
        line += 1
    elif inscope and current == ["m", "u"] and data[line] == "l":
        current.append(data[line])
        line += 1
    elif inscope and current == ["m", "u", "l"] and data[line] == "(":
        current.append(data[line])
        line += 1
    elif inscope and current[:4] == ["m", "u", "l", "("] and data[line].isdigit():
        current.append(data[line])
        current_number.append(data[line])
        line += 1
    elif inscope and current[:4] == ["m", "u", "l", "("] and data[line] == ",":
        current.append(data[line])
        previous_number = current_number[:]
        current_number = []
        line += 1
    elif (
        inscope
        and previous_number != []
        and current[:4] == ["m", "u", "l", "("]
        and data[line].isdigit()
    ):
        current.append(data[line])
        current_number.append(data[line])
        line += 1
    elif (
        inscope
        and previous_number != []
        and current[:4] == ["m", "u", "l", "("]
        and data[line] == ")"
    ):
        current.append(data[line])
        if enabled:
            numbers.append(
                (int("".join(previous_number)), int("".join(current_number)))
            )
        current = []
        previous_number = []
        current_number = []
        inscope = False
        line += 1
    else:
        current = []
        previous_number = []
        current_number = []
        inscope = False
        line += 1

numbers_test = [f"{a},{b}" for (a, b) in numbers]

for item in numbers_test:
    if data.find(item) == -1:
        print(item)

score = sum([a * b for (a, b) in numbers])

# for part 1 disable the enabled check
# check(score, 167090022)

check(score, 89823704)
