## CS104 final project portfolio
## cpu components file. Currently, will have class for the CPU, later will incoporate an ALU and immediate register classes to more fully simulate CPU and incorporate machine code level stuff. Right now will only incorporate Assembly level langauge

from memory import MainMemory, CacheMemory

data_input_file = 'data_input.txt'
instruction_input_file = 'instruction_input.txt'

MEMORY_BUS_SIZE = 128
MAIN_MEMORY_SIZE = 128
CACHE_SIZE = 16
NUMBER_OF_REGISTERS = 9

# CPU class to implement the functionalities of the CPU
# cpu_counter is the index representing the instruction to be parsed
# registers represents the internal registers of the CPU
# cache_flag is a Boolean value determining whether the cache is to be used
# cache is an instance of the CacheMemory for the CPU
# mainmemory is an instance of the MainMemory class for the CPU (obtained through the cache class)

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

    ## methods for interacting with main memory

    def read_from_memory(self, address):
        self.mainmemory.read_from_mainmemory(address)

    def write_to_memory(self, address, data):
        self.mainmemory.write_into_mainmemory(address, data)

    ## assembly language methods

    ## parser methods

