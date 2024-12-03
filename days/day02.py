data = load_data("day02")

grid = [[int(x) for x in line.split(" ")] for line in data.splitlines()]

# print(grid)


def calculate(line):
    diffs = [b - a for a, b in zip(line[:-1], line[1:])]
    if [x for x in diffs if x >= 0] == [] or [x for x in diffs if x <= 0] == []:
        if len([x for x in diffs if abs(x) in range(4)]) == len(diffs):
            return True
    return False


def permutations(line):
    out = []
    for i in range(len(line)):
        new = line[:]
        new.pop(i)
        out.append(new)
    return out


count = 0
for line in grid:
    if calculate(line):
        count += 1

# check(2, count)
check(591, count)


count = 0
for line in grid:
    if any([calculate(x) for x in permutations(line)]):
        count += 1

# check(4, count)
check(621, count)
