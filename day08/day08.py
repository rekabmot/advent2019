filename = "day08/input"

with open(filename) as file_object:
    data = file_object.readline()


# data = "123456789012"

data = list(map(lambda x : int(x), list(data)))

dim_x = 25
dim_y = 6

layer_size = dim_x * dim_y

layer_count = int(len(data) / layer_size)

layers = []

for i in range(0, len(data), layer_size):
    layers.append(data[i:i + layer_size])


def count_digit(digit, layer):
    count = 0

    for i in layer:
        if i == digit:
            count += 1
    
    return count

def get_pixel(x, y, layers):
    index = y * dim_x + x

    for layer in layers:
        if layer[index] == 0:
            return "   "
        elif layer[index] == 1:
            return "xxx"
    return "   "


output = []

for y in range(0, dim_y):
    row = []
    for x in range(0, dim_x):
        row.append(get_pixel(x, y, layers))

    output.append(row)


# for y in range(0, dim_y):
#     row = []

#     for x in range(0, dim_x):
#         for z in range(0, layer_count):
#             if layers[y][x] == 0:
#                 row.append("x")
#                 break
#             elif layers[x][y] == 1:
#                 row.append(" ")
#                 break

    # output.append(row)

joiner = ''
for row in output:
    print(joiner.join(row))

# print(layers)

# layers.sort(key = lambda x: count_digit(0, x))

# print(count_digit(1, layers[0] * count_digit(2, layers[0])))

# print(layers)

# print(count_digit(0, layers[0]))
# print(count_digit(0, layers[1]))



