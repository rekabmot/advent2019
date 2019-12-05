import sys
sys.path.append("c:\\dev\\git\\personal\\advent2019")
from intcode_computer.intcode_computer import IntcodeComputer

filename = "day02/input"

with open(filename) as file_object:
    initial_data = file_object.readline()

computer = IntcodeComputer("1,1,1,4,99,5,6,0,99")

computer.run()

print(computer.memory)

# for x in range(0, 100):
#     for y in range(0, 100):
#         computer.reset()
#         computer.setMemory(1, x)
#         computer.setMemory(2, y)
#         computer.run()

#         if computer.readMemory(0) == 19690720:
#             print(100 * x + y)
#             break

