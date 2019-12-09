
class IntcodeComputer:
  def __init__(self, program):
    self.program = list(map(lambda x : int(x), program.split(",")))
    self.reset()
    self.relative_base = 0

    self.input_function = self.default_input
    self.output_function = self.default_output

  def default_input(self):
    return int(input("-->"))

  def default_output(self, x, context):
    return print(x)

  def reset(self):
    self.memory = list(self.program)

    for i in range(0, 10000):
      self.memory.append(0)
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
    elif mode == 2:
      return self.memory[self.getOffsetAddress(index) + self.relative_base]

  def getOutputParamAddress(self, index, param_modes):
    address = self.getOffsetAddress(index)

    if int(param_modes[-index]) == 2:
      address += self.relative_base

    return address



  def add(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOutputParamAddress(3, param_modes)

    self.memory[z] = x + y
    self.instruction_pointer += 4

  def multiply(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOutputParamAddress(3, param_modes)

    self.memory[z] = x * y
    self.instruction_pointer += 4

  def getInput(self, param_modes):
    x = self.getOutputParamAddress(3, param_modes)
    self.memory[x] = self.input_function()
    self.instruction_pointer += 2

  def printOutput(self, param_modes):
    x = self.getParamValue(1, param_modes)
    self.output_function(x, self)
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
    z = self.getOutputParamAddress(3, param_modes)

    if x < y:
      self.memory[z] = 1
    else:
      self.memory[z] = 0
    
    self.instruction_pointer += 4

  def equals(self, param_modes):
    x = self.getParamValue(1, param_modes)
    y = self.getParamValue(2, param_modes)
    z = self.getOutputParamAddress(3, param_modes)

    if x == y:
      self.memory[z] = 1
    else:
      self.memory[z] = 0

    self.instruction_pointer += 4
  
  def adjust_relative_base(self, param_modes):
    x = self.getParamValue(1, param_modes)
    self.relative_base += x
    self.instruction_pointer += 2

  def get_opcode(self):
    return int(str(self.memory[self.instruction_pointer])[-2:])

  def get_param_modes(self):
    return str(self.memory[self.instruction_pointer])[:-2].zfill(5)

  def run(self):
    self.is_running = True

    opcode = self.get_opcode()
    while self.is_running:
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
      elif opcode == 9:
        self.adjust_relative_base(param_modes)
      elif opcode == 99:
        self.is_running = False      

      opcode = self.get_opcode()