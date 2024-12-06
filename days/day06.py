data = load_data("day06")

def rotate_direction(direction):
  if direction == (0, -1):
    return (1, 0)
  elif direction == (1, 0):
    return (0, 1)
  elif direction == (0, 1):
    return (-1, 0)
  elif direction == (-1, 0):
    return (0, -1)

# grid = [[x for x in line.elems()] for line in data.splitlines()]
directions =  {
  '^': (0, -1),
  '>': (1, 0),
  'v': (0, 1),
  '<': (-1, 0),
}

room = {}
start_position = (None, None)
max_point = (0, 0)
direction = None
for (y, line) in enumerate(data.splitlines()):
  for (x, ch) in enumerate(line.elems()):
    if ch == '#':
      room[(x, y)] = True
    if ch in directions.keys():
      direction = directions[ch]
      start_position = (x, y)
    if x > max_point[0]:
      max_point = (x, max_point[1])
    if y > max_point[1]:
      max_point = (max_point[0], y)

# print(room)
# print(start_pos)
# print(max_point)
# print(direction)

seen = {}
current_position = start_position
# print(current_position)
next_position = (None, None)
for _ in range(100):
  seen[current_position] = True
  next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
  if next_position in room:
    print("next", next_position)
    direction = rotate_direction(direction)
    print("dir", direction)
  
  if next_position[0] < 0 or next_position[1] < 0 or next_position[0] > max_point[0] or next_position[1] > max_point[1]:
    break

  current_position = next_position

# print()
print(current_position)