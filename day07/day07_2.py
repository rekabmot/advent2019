import sys
sys.path.append("d:\\dev\\advent2019")
from intcode_computer.intcode_computer import IntcodeComputer

with open("day07/input") as file_object:
    initial_data = file_object.readline()

with open("day07/permutations2") as file_object:
    permutations = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), file_object.readlines()))

global phases_set
global prev_output

prev_output = 0

def input_function():
    global phases_set
    if phases_set[i] == False:
        phases_set[i] = True
        print("Set phase " + str(phases_set))
        return p[i]
    else:
        return prev_output

def output_function(x, context):
    context.is_running = False
    global prev_output
    # print("Yielding " + str(x))
    prev_output = x

max_result = 0

for p in permutations:
    prev_output = 0
    amps = list(map(lambda x: IntcodeComputer(initial_data), range(0,5)))
    phases_set = [False, False, False, False, False]

    while(amps[0].get_opcode() != 99):
        for i in range(0,5):
            amps[i].input_function = input_function
            amps[i].output_function = output_function

        for i in range(0,5):
            amps[i].run()

    if prev_output > max_result:
        max_result = prev_output

print(max_result)

