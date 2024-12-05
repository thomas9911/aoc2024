data = load_data("day05")


def swapper(array, func):
    # modified bubblesort
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if func(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]


def swap_function(a, b, rules):
    x = rules.get(a)
    if x:
        return b not in x
    return True


[a, b] = data.split("\n\n")

rules = {}
for line in a.splitlines():
    [left, right] = line.split("|")
    rules.setdefault(int(left), []).append(int(right))

for rule in rules.keys():
    rules[rule] = sorted(rules[rule])

results = [[int(x) for x in line.split(",")] for line in b.splitlines()]

part1 = 0
part2 = 0
for result in results:
    new_result = result[:]
    swapper(new_result, lambda a, b: swap_function(a, b, rules))

    middle = len(result) // 2
    if result == new_result:
        part1 += result[middle]
    else:
        part2 += new_result[middle]

check(part1, 4135)
check(part2, 5285)
