data = load_data("day07")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concat(a, b):
    if a == None:
        return b
    return int(str(a) + str(b))


def tryout_part1(items, current_score, current_function, score_to_match):
    if items == []:
        return current_score == score_to_match

    item = items[0]
    next_score = current_function(current_score, item)
    if next_score > score_to_match:
        return False

    return tryout_part1(items[1:], next_score, add, score_to_match) or tryout_part1(
        items[1:], next_score, multiply, score_to_match
    )


def tryout_part2(items, current_score, current_function, score_to_match):
    if items == []:
        return current_score == score_to_match

    item = items[0]
    next_score = current_function(current_score, item)
    if next_score > score_to_match:
        return False

    return (
        tryout_part2(items[1:], next_score, add, score_to_match)
        or tryout_part2(items[1:], next_score, multiply, score_to_match)
        or tryout_part2(items[1:], next_score, concat, score_to_match)
    )


lines = []

for line in data.splitlines():
    [total, rest] = line.split(":")
    total = int(total)
    items = [int(x) for x in rest.split(" ") if x != ""]
    lines.append((total, items))

part1 = 0
for total, items in lines:
    if tryout_part1(items, 0, add, total) or tryout_part1(items, 1, multiply, total):
        part1 += total

# check(part1, 3749)
check(part1, 945512582195)

part2 = 0
for total, items in lines:
    if (
        tryout_part2(items, 0, add, total)
        or tryout_part2(items, 1, multiply, total)
        or tryout_part2(items, None, concat, total)
    ):
        part2 += total

# check(part2, 11387)
check(part2, 271691107779347)
