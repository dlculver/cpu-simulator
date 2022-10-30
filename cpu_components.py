## CS104 final project portfolio
## cpu components file. Currently, will have class for the CPU, later will incoporate an ALU and immediate register classes to more fully simulate CPU and incorporate machine code level stuff. Right now will only incorporate Assembly level langauge

from memory import MainMemory, CacheMemory



# CPU class to implement the functionalities of the CPU
# cpu_counter is the index representing the instruction to be parsed
# registers represents the internal registers of the CPU
# cache_flag is a Boolean value determining whether the cache is to be used
# cache is an instance of the CacheMemory for the CPU
# mainmemory is an instance of the MainMemory class for the CPU (obtained through the cache class)

# helper function: registers in instructions are denoted as "R2", the function extracts the index.
def convert_register_to_index(string):
    return int(string[1:])

class CPU:
    def __init__(self, main_memory_size, cache_size, num_of_registers):
        self.cpu_counter = 0 ## the counter keeps track of where we are in reading instructions
        self.registers = [0]*num_of_registers
        self.cache = CacheMemory(cache_size, main_memory_size)
        self.mainmemory = self.cache.main_memory
        self.main_memory_size = main_memory_size
        self.num_of_registers = num_of_registers
        self.cache_flag = False

    ## cpu counter methods

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = 0

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def get_cpu_counter(self):
        return self.cpu_counter

    ## register methods

    def reset_registers(self):
        self.registers = [0]*self.num_of_registers

    def write_to_register(self, index, value):
        self.registers[index] = value

    ## methods for interacting with cache

    def set_cache_flag(self, value):
        self.cache_flag = value

    def retrieve_from_cache(self, address):
        self.cache.retrieve_from_cache(address)

    def write_to_cache(self, address, data):
        self.cache.write_to_cache(address, data)

    def read_from_cache(self, address):
        self.cache.read_from_cache(address)

    def cache_flush(self):
        for entry in self.cache:
            entry['tag'] = None
            entry['data'] = None

    ## methods for interacting with main memory

    def read_from_memory(self, address):
        self.mainmemory.read_from_mainmemory(address)

    def write_to_memory(self, address, data):
        self.mainmemory.write_into_mainmemory(address, data)

    ## assembly language methods

    def add_instruction(self, rs, rt, rd):
        self.registers[convert_register_to_index(rd)] = self.registers[convert_register_to_index(rs)] + self.registers[convert_register_to_index(rt)]

    def add_i_instruction(self, rs, rd, immediate):
        self.registers[convert_register_to_index(rd)] = self.registers[convert_register_to_index(rs)] + int(immediate)

    def jump_instruction(self, counter):
        self.cpu_counter = int(counter)

    ## the following method implements cache instruction, 0= no cache, 1 = cache on, 2 = cache flush
    def cache_isntruction(self, value):
        if value == 0:
            self.set_cache_flag(False)
        if value == 1:
            self.set_cache_flag(True)
        if value == 2:
            self.cache_flush()

    ## parser methods
    ## instructions are given to the cpu in the format: instruction, register, register, register. The following method
    ## is for parsing such instructions

    def parse_instruction(self, instruction):
        parsed_instruction = instruction.split(',')
        print('Reading instruction:' + instruction)
        if parsed_instruction[0] == 'ADD':
            self.add_instruction(parsed_instruction[1], parsed_instruction[2], parsed_instruction[3])
        if parsed_instruction[0] == 'ADDI':
            self.add_i_instruction(parsed_instruction[1], parsed_instruction[2], parsed_instruction[3])
        if parsed_instruction[0] == 'J':
            self.jump_instruction(parsed_instruction[1])
        if parsed_instruction[0] == 'CACHE':
            self.cache_isntruction(parsed_instruction[1])



