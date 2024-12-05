data = load_data("day04")


def make_diagonal(lines):
    out = []

    for y, line in enumerate(lines):
        for x, val in enumerate(line.elems()):
            new_row = x + y
            if new_row >= len(out):
                out.append([])
            out[new_row].append(val)

    return ["".join(x) for x in out]


def make_rotate(lines):
    length = len(lines)
    # when have to use the range list comprehension
    # because python will reuse the same list :'(
    # (references the same list)
    out = [[None] * length for _ in range(length)]
    size = len(lines) - 1

    for y, line in enumerate(lines):
        for x, val in enumerate(line.elems()):
            new_x = size - y
            new_y = x
            out[new_y][new_x] = val

    return ["".join(x) for x in out]


def inner_finder(line, needle, sub_score):
    index = line.find(needle)
    if index == -1:
        return sub_score
    return inner_finder(line[index + 1 :], needle, sub_score + 1)


def finder(line, score):
    score += inner_finder(line, "XMAS", 0)
    score += inner_finder(line, "SAMX", 0)
    return score


def map_getter(map, x, y, default="."):
    return map.get(y, {}).get(x, default)


lines = data.splitlines()
diagonal = make_diagonal(lines)
rotated = make_rotate(lines)
diagonal_rotated = make_diagonal(rotated)

score = 0

for line in lines:
    score = finder(line, score)

for line in rotated:
    score = finder(line, score)

for line in diagonal:
    score = finder(line, score)

for line in diagonal_rotated:
    score = finder(line, score)

check(score, 2554)
# check(score, 18)

score = 0

line_map = {}
for y, line in enumerate(lines):
    for x, val in enumerate(line.elems()):
        line_map.setdefault(y, {})[x] = val

for y, line in enumerate(lines):
    for x, val in enumerate(line.elems()):
        if val == "A":
            one = "".join(
                [
                    map_getter(line_map, x - 1, y - 1),
                    map_getter(line_map, x, y),
                    map_getter(line_map, x + 1, y + 1),
                ]
            )
            two = "".join(
                [
                    map_getter(line_map, x + 1, y - 1),
                    map_getter(line_map, x, y),
                    map_getter(line_map, x - 1, y + 1),
                ]
            )

            if one in ["MAS", "SAM"] and two in ["MAS", "SAM"]:
                score += 1

check(score, 1916)
# check(score, 9)
