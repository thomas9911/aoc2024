data = load_data("day13")

A = 3
B = 1

def equation_to_int(text):
  if text.startswith("X+"):
    return int(text.split("X+")[1])
  if text.startswith("Y+"):
    return int(text.split("Y+")[1])
  if text.startswith("X="):
    return int(text.split("X=")[1])
  if text.startswith("Y="):
    return int(text.split("Y=")[1])

def determinant(item, left, right):
  return (item[left][0] * item[right][1]) - (item[left][1] * item[right][0])

def scoring(a, b):
  return a * A + b * B

def make_item(text, add_to_prize):
  item = {
    "a": None,
    "b": None,
    "prize": None,
  }
  for line in text.splitlines():
    coords = None
    prize = False
    button_a = False
    button_b = False
    if line.startswith("Button A: "):
      coords = line.split("Button A: ")[1]
      button_a = True
    elif line.startswith("Button B: "):
      coords = line.split("Button B: ")[1]
      button_b = True
    elif line.startswith("Prize: "):
      coords = line.split("Prize: ")[1]
      prize = True

    if coords == None:
      fail("empty!")

    [x,y] = [equation_to_int(part) for part in coords.split(", ")]
    if button_a:
      item["a"] = (x,y)
    elif button_b:
      item["b"] = (x,y)
    elif prize:
      item["prize"] = (x+add_to_prize,y+add_to_prize)
  return item

def calculate_score(item):
  base = determinant(item, "a", "b")

  a_det = determinant(item, "a", "prize")
  b_det = determinant(item, "b", "prize")

  a = b_det / base
  b = a_det / base

  if a % 1 == 0.0 and b % 1 == 0.0:
    a = abs(int(a))
    b = abs(int(b))
  else:
    return 0

  return scoring(a, b)

score = 0
for x in data.split("\n\n"):
  item = make_item(x, 0)
  score += calculate_score(item)

check(score, 40369)

score = 0
for x in data.split("\n\n"):
  item = make_item(x, 10000000000000)
  score += calculate_score(item)

check(score, 72587986598368)
