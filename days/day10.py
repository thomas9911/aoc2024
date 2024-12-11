data = load_data("day10").strip()
EXAMPLE_PLACEHOLDER_VALUE = 15
grid = [
    [EXAMPLE_PLACEHOLDER_VALUE if x == "." else int(x) for x in line.elems()]
    for line in data.splitlines()
]

rows = len(grid)
cols = len(grid[0])
options = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def get_neighbours_base(current_x, current_y, path, results, filter):
    (previous_x, previous_y) = path[-1]
    if grid[previous_x][previous_y] == 9:
        if filter(path, results):
            results.append(path)
        if results == []:
            results.append(path)
        return

    current_height = grid[current_x][current_y]
    for dx, dy in options:
        x, y = current_x + dx, current_y + dy
        if (
            x >= 0
            and x < rows
            and y >= 0
            and y < cols
            and current_height + 1 == grid[x][y]
            and (x, y) not in path
        ):
            next_path = path[:]
            next_path.append((x, y))
            get_neighbours_base(x, y, next_path, results, filter)


def get_neighbours_unique(current_x, current_y, path, results):
    filter = lambda path, results: not any(
        [result[0] == path[0] and result[-1] == path[-1] for result in results]
    )
    return get_neighbours_base(current_x, current_y, path, results, filter)


def get_neighbours_all(current_x, current_y, path, results):
    filter = lambda path, results: True
    return get_neighbours_base(current_x, current_y, path, results, filter)


def calculate_trailheads_score(starting_positions):
    score = 0
    for current_x, current_y in starting_positions:
        results = []
        get_neighbours_unique(current_x, current_y, [(current_x, current_y)], results)
        score += len(results)
    return score


def calculate_trailheads_rating(starting_positions):
    score = 0
    for current_x, current_y in starting_positions:
        results = []
        get_neighbours_all(current_x, current_y, [(current_x, current_y)], results)
        score += len(results)
    return score


starting_positions = []

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == 0:
            starting_positions.append((r, c))

check(782, calculate_trailheads_score(starting_positions))  # part1
check(1694, calculate_trailheads_rating(starting_positions))  # part2
