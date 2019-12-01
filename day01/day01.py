import math

def get_fuel(mass):
    return math.floor(mass / 3) - 2

def process_module(mass):
    total = 0

    fuel_required = get_fuel(mass)
    total += fuel_required

    while (fuel_required > 0):
        fuel_required = get_fuel(fuel_required)
        total += max(fuel_required, 0)
    
    return total

filename = "day01/input"

with open(filename) as file_object:
    lines = file_object.readlines()

result = 0

for line in lines:
    module = int(line)
    result += process_module(module)

print(result)