data = load_data("day08")


def pivot(a, b):
    return pivot_n(a, b, 1)


def pivot_n(a, b, n):
    return (n * (b[0] - a[0]) + b[0], n * (b[1] - a[1]) + b[1])


def combinations(list):
    out = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            out.append((list[i], list[j]))
            out.append((list[j], list[i]))
    return out


def print_grid(map, antinodes, max_x, max_y):
    for y in range(0, max_y + 1):
        line = ""
        for x in range(0, max_x + 1):
            antenna = map.get((x, y))
            antinode = antinodes.get((x, y))
            if antenna:
                line += antenna
            elif antinode:
                line += "#"
            else:
                line += "."
        print(line)


map = {}
lookup_map = {}
max_x = 0
max_y = 0
for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line.elems()):
        if char != ".":
            map[(x, y)] = char
            lookup_map.setdefault(char, []).append((x, y))
        if x > max_x:
            max_x = x
    if y > max_y:
        max_y = y

antinodes = {}

for key in lookup_map.keys():
    for a, b in combinations(lookup_map[key]):
        antinode = pivot(a, b)
        if (
            antinode[0] >= 0
            and antinode[0] <= max_x
            and antinode[1] >= 0
            and antinode[1] <= max_y
        ):
            antinodes[antinode] = True


# print_grid(map, antinodes, max_x, max_y)
part1 = len(antinodes.keys())
check(329, part1)
# check(14, part1)

antinodes = {}

for key in lookup_map.keys():
    for a, b in combinations(lookup_map[key]):
        for n in range(0, 50):
            antinode = pivot_n(a, b, n)
            if (
                antinode[0] >= 0
                and antinode[0] <= max_x
                and antinode[1] >= 0
                and antinode[1] <= max_y
            ):
                antinodes[antinode] = True
            else:
                break

# print_grid(map, antinodes, max_x, max_y)

part2 = len(antinodes.keys())
# check(34, part2)
check(1190, part2)
