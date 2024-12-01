data = load_data("day01")

lefts = []
rights = []

def get_insert_position(item, list, starting_point):
    if len(list) == 0:
        return 0
    
    if len(list) == 1:
        if item >= list[0]:
            return starting_point + 1
        else:
            return starting_point

    pivot = len(list) // 2
    if item >= list[pivot]:
        return get_insert_position(item, list[pivot:], starting_point + pivot)
    else:
        return get_insert_position(item, list[:pivot], starting_point)

for line in data.splitlines():
    [left, right] = [int(x) for x in line.split("   ")]
    insert_position = get_insert_position(right, rights, 0)
    rights.insert(insert_position, right)

    insert_position = get_insert_position(left, lefts, 0)
    lefts.insert(insert_position, left)

# start part 1:

result = 0

for (a, b) in zip(lefts, rights):
    if b <= a:
        result += (a - b)
    else:
        result += (b - a)

check(result, 3508942)
# check(result, 11)

# end part 1

# start part 2:

def make_counter(list):
    counter = {}
    for item in list:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1
    return counter

left_counter = make_counter(lefts)
right_counter = make_counter(rights)

score = 0

for key, value in left_counter.items():
    if key in right_counter:
        score += key * value * right_counter[key]

# check(score, 31)
check(score, 26593248)

# end part 2
