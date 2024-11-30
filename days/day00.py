data = load_data("day00")

numbers = [[int(x) for x in line.split(",")] for line in data.strip().splitlines()]

check([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], numbers)
