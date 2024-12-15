data = load_data("day15").strip().replace("\r\n", "\n")

BOX = "O"
WALL = "#"
ROBOT = "@"
EMPTY = "."
directions = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}
reverse_dirs = {v: k for k, v in directions.items()}

[board_data, commands_data] = data.split("\n\n")
commands_data = commands_data.replace("\n", "")


def parse_board(text):
    board = {}
    current_pos = None
    for y, line in enumerate(text.splitlines()):
        for x, c in enumerate(line.elems()):
            if c == BOX:
                board[(x, y)] = BOX
            elif c == WALL:
                board[(x, y)] = WALL
            elif c == ROBOT:
                current_pos = (x, y)
    return (current_pos, board)


def parse_commands(text):
    commands = []
    for x in text.elems():
        commands.append(directions[x])
    return commands


def try_move_box(pos, new_pos, command, board):
    (dx, dy) = command
    for n in range(2, 100):
        next_pos = (pos[0] + dx * n, pos[1] + dy * n)
        if next_pos not in board:
            board[next_pos] = BOX
            board.pop(new_pos)
            return (new_pos, board)
        elif board[next_pos] == BOX:
            continue
        elif board[next_pos] == WALL:
            return (pos, board)
    fail("ran out of loop! in try_move_box")


def apply_command(pos, command, board):
    (dx, dy) = command
    new_pos = (pos[0] + dx, pos[1] + dy)
    if new_pos in board:
        found = board[new_pos]
        if found == WALL:
            return (pos, board)
        elif found == BOX:
            return try_move_box(pos, new_pos, command, board)
    else:
        return (new_pos, board)


def print_board(board, current_position):
    for y in range(12):
        buffer = []
        for x in range(12):
            if (x, y) == current_position:
                buffer.append("@")
                continue
            val = board.get((x, y), ".")
            buffer.append(val)
        print("".join(buffer))


(current_position, board) = parse_board(board_data)
commands = parse_commands(commands_data)

for command in commands:
    (current_position, board) = apply_command(current_position, command, board)

score = 0
for (x, y), val in board.items():
    if val == BOX:
        score += y * 100 + x

check(score, 1568399)
