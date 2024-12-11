data = load_data("day11").strip()


def trim_zeros(stone):
    return str(int(stone))


STONE_CACHE = {"0": ["1"]}
CACHE_STAT = {"hit": 0, "mis": 0}


def apply_per_stone(stone):
    if stone in STONE_CACHE:
        CACHE_STAT["hit"] += 1
        return STONE_CACHE[stone]
    else:
        CACHE_STAT["mis"] += 1

    if len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        left, right = stone[:midpoint], trim_zeros(stone[midpoint:])
        STONE_CACHE[stone] = [left, right]
        return [left, right]
    else:
        stone_int = int(stone)
        new_stone = str(stone_int * 2024)
        STONE_CACHE[stone] = [new_stone]
        return [new_stone]


def apply_rounds(stones, rounds):
    stones_lookup = {}
    for stone in stones:
        stones_lookup[stone] = stones_lookup.setdefault(stone, 0) + 1

    for _ in range(rounds):
        next_lookup = {}
        for stone in stones_lookup:
            for next_stone in apply_per_stone(stone):
                next_lookup[next_stone] = (
                    next_lookup.setdefault(next_stone, 0) + stones_lookup[stone]
                )
        stones_lookup = next_lookup

    score = 0
    for counts in stones_lookup.values():
        score += counts

    return score


stones = [x for x in data.split(" ")]

part1 = apply_rounds(stones, 25)
check(part1, 188902)

part2 = apply_rounds(stones, 75)
check(part2, 223894720281135)

stat = (
    int((CACHE_STAT["hit"] / (CACHE_STAT["hit"] + CACHE_STAT["mis"])) * 10000)
) / 100
print(f"cache hit ration: {stat}%")
