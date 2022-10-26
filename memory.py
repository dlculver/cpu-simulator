## CS104 codecademy portfolio project
## implementing Memory Parent class, all other forms of memory in this project, e.g. the Main Memory and Cache Memory
## will be written as Child classes based on Memory.
## addresses will be written in binary



## main memory class
class MainMemory:
    def __init__(self, size):
        self.size = size
        self.main_memory = {}
        self.initialize_main_memory()


    def __str__(self):
        string = ''
        for key, value in self.main_memory.items():
            string += f'({key}, {str(value)})\n'
        return string


    def initialize_main_memory(self):
        for i in range(self.size):
            self.main_memory['{0:08b}'.format(i)] = 0

    ## addresses must be given in binary
    def read_from_mainmemory(self, address):
        if type(address) == int:
            address = '{0:08b}'.format(address)
        data = self.memory[address]
        return data

    def write_into_mainmemory(self, address, data):
        if type(address) == int:
            address = '{0:08b}'.format(address)
        print(f'CPU writing to main memory at address {address}: {data}')
        self.main_memory[address] = data

## adding idx associated to cache for implementing FIFO or other replacement methods, might change later
# class CacheMemory:
#     def __init__(self, size, idx):
#         self.size = size
#         self.idx = idx
#         self.memory = [{'tag':None, 'data': None}] * self.size
#
#     def retrieve_from_cache(self, idx):## finish tomorrow
