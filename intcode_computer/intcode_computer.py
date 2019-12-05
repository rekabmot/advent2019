
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

  def getParamValue(self, index, param_modes):
    mode = int(param_modes[-index])

    if mode == 0:
      return self.memory[self.getOffsetAddress(index)]
    elif mode == 1:
      return self.memory[self.instruction_pointer + index]


  def add(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOffsetAddress(3)

    self.memory[z] = x + y
    self.instruction_pointer += 4

  def multiply(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOffsetAddress(3)

    self.memory[z] = x * y
    self.instruction_pointer += 4

  def getInput(self, param_modes):
    x = self.getParamValue(1, "1")
    self.memory[x] = int(input("-->"))
    self.instruction_pointer += 2

  def printOutput(self, param_modes):
    x = self.getParamValue(1, param_modes)
    print(x)
    self.instruction_pointer += 2

  def jump_true(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)

    if x != 0:
      self.instruction_pointer = y
    else:
      self.instruction_pointer += 3

  def jump_false(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)

    if x == 0:
      self.instruction_pointer = y
    else:
      self.instruction_pointer += 3

  def less_than(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOffsetAddress(3)

    if x < y:
      self.memory[z] = 1
    else:
      self.memory[z] = 0
    
    self.instruction_pointer += 4


  def equals(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOffsetAddress(3)

    if x == y:
      self.memory[z] = 1
    else:
      self.memory[z] = 0

    self.instruction_pointer += 4

  def get_opcode(self):
    return int(str(self.memory[self.instruction_pointer])[-2:])

  def get_param_modes(self):
    return str(self.memory[self.instruction_pointer])[:-2].zfill(5)

  def run(self):
    opcode = self.get_opcode()
    while opcode != 99:
      param_modes = self.get_param_modes()

      if opcode == 1:
        self.add(param_modes)
      elif opcode == 2:
        self.multiply(param_modes)
      elif opcode == 3:
        self.getInput(param_modes)
      elif opcode == 4:
        self.printOutput(param_modes)
      elif opcode == 5:
        self.jump_true(param_modes)
      elif opcode == 6:
        self.jump_false(param_modes)
      elif opcode == 7:
        self.less_than(param_modes)
      elif opcode == 8:
        self.equals(param_modes)

      opcode = self.get_opcode()