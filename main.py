## CS104 portfolio project
## main file

from memory import MainMemory, CacheMemory
from cpu_components import CPU

data_input_file = 'data_input.txt'
instruction_input_file = 'instruction_input.txt'

MEMORY_BUS_SIZE = 128
MAIN_MEMORY_SIZE = 128
CACHE_SIZE = 16
NUMBER_OF_REGISTERS = 9



# generates list of instructions from .txt file

def fetch_instructions(input_txt):
    instruction_file = open(input_txt, "r")
    instructions = instruction_file.readlines()
    instructions = list(map(lambda s: s.strip(), instructions))
    return instructions

def download_data(input_data):
    data_file = open(input_data, 'r')
    data = data_file.readlines()
    data = list(map(lambda s: s.strip, data))
    return data

## initializes memory in cpu
def initialize_memory(cpu, input_data):
    data_loaded = download_data(input_data)
    for data in data_loaded:
        data_parsed = data.split(',')
        cpu.mainmemory.write_into_mainmemory(data_parsed[0], data_parsed[1])

## send instructions to cpu
def send_instructions(cpu, input_txt):
    input_instructions = fetch_instructions(input_txt)
    for instruction in input_instructions:
        cpu.parse_instruction(instruction)


## start cpu
cpu = CPU(MAIN_MEMORY_SIZE,CACHE_SIZE,NUMBER_OF_REGISTERS)
print("---------------------------------------------------")
print("Welcome to the Python CPU Simulator!")
print("---------------------------------------------------")
print("Initializing Memory from data input file...")
initialize_memory(cpu, data_input_file)
print("Memory successfully initialized")
print("---------------------------------------------------")
print("Sending instructions to CPU...")
send_instructions(cpu, instruction_input_file)
print("---------------------------------------------------")
print("Terminating CPU Processing...")
