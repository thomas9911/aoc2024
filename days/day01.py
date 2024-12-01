def get_insert_position(item: int, list: list[int], starting_point: int):
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


def make_counter(list: list[int]) -> dict[int, int]:
    counter = {}
    for item in list:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1
    return counter


def add_to_list_ordered(item: int, list: list[int]):
    insert_position = get_insert_position(item, list, 0)
    list.insert(insert_position, item)
    return list


data = load_data("day01")

lefts = []
rights = []

for line in data.splitlines():
    [left, right] = [int(x) for x in line.split("   ")]
    add_to_list_ordered(right, rights)
    add_to_list_ordered(left, lefts)

# part 1:

result = sum([abs(b - a) for a, b in zip(lefts, rights)])

check(result, 3508942)
# check(result, 11)

# part 2:

left_counter = make_counter(lefts)
right_counter = make_counter(rights)

## classic loop
# score = 0

# for key, value in left_counter.items():
#     if key in right_counter:
#         score += key * value * right_counter[key]

## list comprehension
score = sum(
    [
        key * value * right_counter[key]
        for key, value in left_counter.items()
        if key in right_counter
    ]
)

# check(score, 31)
check(score, 26593248)

# end part 2
