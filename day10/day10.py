import math

class Vector2:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def to(self, target):
    return Vector2(target.x - self.x, target.y - self.y)
  
  def magnitude(self):
    return math.sqrt(self.x * self.x + self.y * self.y)

  def normalized(self):
    mag = self.magnitude()
    return Vector2(round(self.x / mag, 8), round(self.y / mag, 8))


filename = "day10/input"

with open(filename) as file_object:
    lines = file_object.readlines()


asteroids = []

y = 0
for line in lines:
  row = list(line)
  
  for x in range(0, len(row)):
    if row[x] == "#":
      asteroids.append(Vector2(x, y))
    
  y += 1

def count_los(source, asteroids):
  vectors = []
  los = 0
  for asteroid in asteroids:
    if asteroid == source:
      continue

    vector = source.to(asteroid).normalized()

    if vector not in vectors:
      vectors.append(vector)
      los += 1

  return los

los_count = []
for asteroid in asteroids:
  los_count.append(count_los(asteroid, asteroids))

los_count.sort()

print(los_count)