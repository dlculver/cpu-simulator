## CS104 final project portfolio
## cpu components file. Currently, will have class for the CPU, later will incoporate an ALU and immediate register classes to more fully simulate CPU and incorporate machine code level stuff. Right now will only incorporate Assembly level langauge

from memory import MainMemory

MEMORY_BUS_SIZE = 128
MAIN_MEMORY_SIZE = 128
CACHE_SIZE = 16
NUMBER_OF_REGISTERS = 9

class CPU:
    def __init__(self, main_memory_size, cache_size, num_of_registers):
        self.cpu_counter = 0 ## the counter keeps track of where we are in reading instructions
        self.registers = [0]*num_of_registers
        self.memory = MainMemory(main_memory_size)
        self.main_memory_size = main_memory_size
        self.num_of_registers = num_of_registers

    ## cpu counter methods

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = 0

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    ## register methods

    def reset_registers(self):
        self.registers = [0]*self.num_of_registers

    ## methods for interacting with cache

    ## methods for interacting with main memory

    ## assembly language methods

