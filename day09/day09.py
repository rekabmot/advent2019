import sys
sys.path.append("d:\\dev\\advent2019")
from intcode_computer.intcode_computer import IntcodeComputer

filename = "day09/input"

with open(filename) as file_object:
    program = file_object.readline()

computer = IntcodeComputer(program)

computer.run()

