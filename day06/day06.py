filename = "day06/input"

with open(filename) as file_object:
  initial_data = file_object.read().splitlines()

def count_orbits(x):
  count = 0

  while orbits[x] != "COM":
    x = orbits[x]
    count += 1
  
  return count + 1

def get_orbits(x):
  path = [x]

  while orbits[x] != "COM":
    x = orbits[x]
    path.append(x)
  
  return path

orbits = {}

for d in initial_data:
  split = d.split(")")
  orbits[split[1]] = split[0]

# total = 0

# for k in orbits.keys():
#   total += count_orbits(k)

# print(total)

my_orbits = get_orbits("YOU")
san_orbits = get_orbits("SAN")

print(my_orbits)
print(san_orbits)

while(my_orbits[-1] == san_orbits[-1]):
  my_orbits.pop()
  san_orbits.pop()

print(my_orbits)
print(san_orbits)

print((len(my_orbits) - 1) + (len(san_orbits) - 1))