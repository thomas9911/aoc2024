data = load_data("day14").strip()

dev = False

if dev:
    ROWS = 7
    COLS = 11
else:
    ROWS = 103
    COLS = 101


def parse_line(text):
    entries = [tuple([int(y) for y in x.split(",")]) for x in text[2:].split(" v=")]
    return entries


def calculate(start, velocity, rounds, length):
    return (start + velocity * rounds) % length


def after_n_rounds(point, velocity, rounds):
    return (
        calculate(point[0], velocity[0], rounds, COLS),
        calculate(point[1], velocity[1], rounds, ROWS),
    )


def to_quadrant(point):
    if point[0] < COLS // 2 and point[1] < ROWS // 2:
        return 0
    if point[0] > COLS // 2 and point[1] < ROWS // 2:
        return 1
    if point[0] < COLS // 2 and point[1] > ROWS // 2:
        return 2
    if point[0] > COLS // 2 and point[1] > ROWS // 2:
        return 3
    return None


def grid_after_n_rounds(info, rounds):
    grid = {}

    for [point, velocity] in info:
        position = after_n_rounds(point, velocity, rounds)
        grid[position] = grid.get(position, 0) + 1

    return grid


def print_grid(grid):
    for y in range(ROWS):
        buffer = []
        for x in range(COLS):
            value = grid.get((x, y))
            if value:
                buffer.append("X")
            else:
                buffer.append(".")
        print("".join(buffer))


def possible_contains_tree(grid):
    for y in range(ROWS):
        possible = 0
        for x in range(COLS):
            value = grid.get((x, y))
            if value != None:
                possible += 1
            else:
                possible = 0
            if possible > 7:
                # 7 in a row is too much of a coincidence
                return True
    return False


info = [parse_line(x) for x in data.splitlines()]
grid = grid_after_n_rounds(info, 100)

scores = [0, 0, 0, 0]
for x in range(COLS):
    for y in range(ROWS):
        quadrant = to_quadrant((x, y))
        if quadrant != None:
            add_it = grid.get((x, y), 0)
            scores[quadrant] += add_it

safety_factor = scores[0] * scores[1] * scores[2] * scores[3]
check(safety_factor, 233709840)

for rounds in range(6500, 6800):
    grid = grid_after_n_rounds(info, rounds)
    if possible_contains_tree(grid):
        final = rounds
        break

check(final, 6620)
