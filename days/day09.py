data = load_data("day09").strip()

def build_layout(data):
  layout = []

  current_id = 0

  on_spacing = False
  for ch in data.elems():
    number = int(ch)
    for _ in range(number):
      if on_spacing:
        layout.append(None)
      else:
        layout.append(current_id)
    if on_spacing:
      current_id += 1
      on_spacing = False
    else:
      on_spacing = True

  return layout

def compact_layout(layout):
  for _ in range(len(layout)):
    if None in layout:
      item = layout.pop()
      if item == None:
        continue
      index = layout.index(None)
      layout[index] = item
    else:
      break

def checksum(layout):
  score = 0
  for (i, item) in enumerate(layout):
    score += i * item
  return score

layout = build_layout(data)
# print(layout)
compact_layout(layout)
# print(layout)
print(checksum(layout))
