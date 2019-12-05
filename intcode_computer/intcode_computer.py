
class IntcodeComputer:
  def __init__(self, program):
    self.program = list(map(lambda x : int(x), program.split(",")))
    self.reset()

  def reset(self):
    self.memory = list(self.program)
    self.instruction_pointer = 0

  def setMemory(self, address, value):
    self.memory[address] = value

  def readMemory(self, address):
    return self.memory[address]

  def getOffsetAddress(self, offset):
    return self.memory[self.instruction_pointer + offset]

  def getparamValue(self, index, param_modes):
    mode = int(param_modes[-index])

    if mode == 0:
      return self.memory[self.getOffsetAddress(index)]
    elif mode == 1:
      return self.memory[self.memory[index]]


  def add(self, param_modes):
    modes = param_modes.zfill(3)

    x = self.getparamValue(1, modes)
    y = self.getparamValue(2, modes)
    z = self.getOffsetAddress(3)

    self.memory[z] = x + y
    self.instruction_pointer += 4

  def multiply(self, param_modes):
    modes = param_modes.zfill(3)

    x = self.getparamValue(1, modes)
    y = self.getparamValue(2, modes)
    z = self.getOffsetAddress(3)

    self.memory[z] = x * y
    self.instruction_pointer += 4

  def getInput(self):
    x = self.getparamValue(1, "1")
    self.memory[x] = input("-->")
    self.instruction_pointer += 2

  def printOutput(self):
    x = self.getparamValue(1, "1")
    print(self.memory[x])
    self.instruction_pointer += 2

  def get_opcode(self):
    return int(str(self.memory[self.instruction_pointer])[-2:])

  def get_param_modes(self):
    return str(self.memory[self.instruction_pointer])[:-2]

  def run(self):
    opcode = self.get_opcode()
    while opcode != 99:
      print(opcode)
      param_modes = self.get_param_modes()

      if opcode == 1:
        self.add(param_modes)
      elif opcode == 2:
        self.multiply(param_modes)
      elif opcode == 3:
        self.getInput()
      elif opcode == 4:
        self.printOutput()
      
      opcode = self.get_opcode()