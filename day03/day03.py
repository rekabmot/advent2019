filename = "day03/input"

class Command:
  def __init__(self, direction, distance):
    self.direction = direction
    self.distance = distance

  def __str__(self):
    return self.direction + " : " + self.distance

def parse_line(line):
  return list(map(lambda x: Command(x[0:1], int(x[1:])), line.split(",")))


with open(filename) as file_object:
  path_1 = parse_line(file_object.readline())
  path_2 = parse_line(file_object.readline())

actions = {
  "R": lambda x, y: (x + 1, y),
  "L": lambda x, y: (x - 1, y),
  "U": lambda x, y: (x, y + 1),
  "D": lambda x, y: (x, y - 1)
}

def key(x, y):
  return str(x) + ":" + str(y)

grid = {}
x, y = 0, 0
steps = 0

for command in path_1:
  action = actions[command.direction]
  for i in range(0, command.distance):
    x, y = action(x, y)
    steps += 1

    if key(x,y) in grid:
      grid[key(x,y)] = min(grid[key(x,y)], steps)
    else:
      grid[key(x,y)] = steps

intersections = []
x, y = 0, 0
steps = 0

for command in path_2:
  action = actions[command.direction]
  for i in range(0, command.distance):
    x, y = action(x, y)
    steps += 1
    if key(x,y) in grid:      
      intersections.append(grid[key(x,y)] + steps)

print(min(intersections))