data = load_data("day07")


def log_10_at_home(a):
    # calculates the number of times a number can be divided by 10
    rounds = 0
    for _ in range(100):
        if a > 9:
            a /= 10
            rounds += 1
        elif a < 1:
            rounds -= 1
            break
        else:
            break
    return rounds


def power10(a, b):
    # calculates a * 10 ** b
    base = 1
    for i in range(b):
        base *= 10
    return a * base


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concat(a, b):
    if a == None:
        return b
    return power10(a, log_10_at_home(b) + 1) + b


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
