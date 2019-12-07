import sys
sys.path.append("d:\\dev\\advent2019")
from intcode_computer.intcode_computer import IntcodeComputer

with open("day07/input") as file_object:
    initial_data = file_object.readline()

with open("day07/permutations") as file_object:
    permutations = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), file_object.readlines()))

print(permutations)

computer = IntcodeComputer(initial_data)

def test_permutation(permutation):
    global prev_result
    prev_result = 0

    for i in permutation:
        inputs = [i, prev_result]
        global z
        z = 0

        def input_method():
            global z
            #print(inputs[z])
            q = inputs[z]
            z += 1
            return q
        
        def output_method(x):
            global prev_result
            prev_result = x

        computer.input_function = input_method
        computer.output_function = output_method
        computer.reset()
        computer.run()
    
    return prev_result

result = 0

for p in permutations:
    r = test_permutation(p)
    
    if r > result:
        print(result)
        result = r

print(result)