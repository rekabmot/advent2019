import sys
sys.path.append("c:\\dev\\git\\personal\\advent2019")
from intcode_computer.intcode_computer import IntcodeComputer

filename = "day05/input"

with open(filename) as file_object:
    initial_data = file_object.readline()
    
computer = IntcodeComputer(initial_data)

computer.run()