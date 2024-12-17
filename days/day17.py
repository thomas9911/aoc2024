data = load_data("day17").strip().replace("\r\n", "\n")

tests = False

[state_text, program_text] = data.split("\n\n")

program = [int(x) for x in program_text.strip().split("Program: ")[1].split(",")]

def new_state():
  return {
    "a": 0,
    "b": 0,
    "c": 0,
    "pc": 0,
    "out": []
  }

def parse_state(state_text):
  state = new_state()

  for line in state_text.splitlines():
    if line.startswith("Register A: "):
      state["a"] = int(line.split("Register A: ")[1])
    if line.startswith("Register B: "):
      state["b"] = int(line.split("Register B: ")[1])
    if line.startswith("Register C: "):
      state["c"] = int(line.split("Register C: ")[1])

  return state

def to_power2(input):
  return 1 << input

def to_value(state, value):
  if value <= 3:
    return value
  if value == 4:
    return state["a"]
  if value == 5:
    return state["b"]
  if value == 6:
    return state["c"]
  if value == 7:
    fail("invalid program")

def adv(state, input):
  state["a"] = state["a"] // to_power2(to_value(state, input))
  return True

def bxl(state, input):
  state["b"] = state["b"] ^ input
  return True

def bst(state, input):
  state["b"] = to_value(state, input) % 8
  return True

def jnz(state, input):
  if state["a"] == 0:
    return True
  else:
    state["pc"] = input
    return False

def bxc(state, input):
  state["b"] = state["b"] ^ state["c"]
  return True

def out(state, input):
  state["out"].append(to_value(state, input) % 8)
  return True

def bdv(state, input):
  state["b"] = state["a"] // to_power2(to_value(state, input))
  return True

def cdv(state, input):
  state["c"] = state["a"] // to_power2(to_value(state, input))
  return True

def run(state, program, rounds=1000):
  for _ in range(rounds):
    if apply(state, program):
      return state
  fail("loop ran out")

commands = {
  0: adv,
  1: bxl,
  2: bst,
  3: jnz,
  4: bxc,
  5: out,
  6: bdv,
  7: cdv
}

def apply(state, program):
  command = program[state["pc"]]
  input = program[state["pc"] + 1]
  if commands[command](state, input):
    state["pc"] += 2

  if len(program) <= state["pc"]:
    return True
  return False

if tests:
  x = new_state()
  x["c"] = 9
  run(x, [2,6])
  check(x["b"], 1)

  x = new_state()
  x["a"] = 10
  run(x, [5,0,5,1,5,4])
  check(x["out"], [0,1,2])

  x = new_state()
  x["a"] = 2024
  run(x, [0,1,5,4,3,0])
  check(x["out"], [4,2,5,6,7,7,7,7,3,1,0])
  check(x["a"], 0)

  x = new_state()
  x["b"] = 29
  run(x, [1,7])
  check(x["b"], 26)

  x = new_state()
  x["b"] = 2024
  x["c"] = 43690
  run(x, [4,0])
  check(x["b"], 44354)

state = parse_state(state_text)
run(state, program)
part1 = ",".join([str(x) for x in state["out"]])
check(part1, "3,6,3,7,0,7,0,3,0")

# UPPER = 281500000000000
# LOWER = 35100000000000

# current_high = UPPER
# current_low = LOWER
# mid = None

# for _ in range(100):
#   mid = (current_high - current_low) // 2 + current_low
#   print(mid)
#   state["a"] = mid
#   state["pc"] = 0
#   state["out"] = []
#   run(state, program)

#   print(state["out"])
#   if len(program) > len(state["out"]):
#     current_low = mid
#     continue
#   if len(program) < len(state["out"]):
#     current_high = mid
#     continue

#   for i in range(2):
#     if program[i] > state["out"][i]:
#       current_low = (current_low * 3) // 2
#       break
#     elif program[i] < state["out"][i]:
#       current_high = (current_high * 2) // 3
#       break
