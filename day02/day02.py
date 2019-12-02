filename = "day02/input"

with open(filename) as file_object:
    initial_data = list(map(lambda x : int(x), file_object.readline().split(",")))




def add(x, y, dest, data):
    data[dest] = data[x] + data[y]

def multiply(x, y, dest, data):
    data[dest] = data[x] * data[y]

def finish(data):
    if (data[0] == 19690720):
        print(100 * data[1] + data[2])

def run(noun, verb, initial_data):
    data = list(initial_data)

    data[1] = noun
    data[2] = verb

    for i in range(0, len(data), 4):
        opcode = data[i]
        if opcode == 1:
            add(data[i + 1], data[i + 2], data[i + 3], data)
        elif opcode == 2:
            multiply(data[i + 1], data[i + 2], data[i + 3], data)
        else:
            finish(data)

for x in range(0, 100):
    for y in range(0, 100):
        run(x, y, initial_data)