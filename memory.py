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
        if self.get(address) is not None:
            data = self.memory[address]
            return data
        print(f"No data found Main Memory at {address}", end = "")
        return None

    def write_into_mainmemory(self, address, data):
        if type(address) == int:
            address = '{0:08b}'.format(address)
        print(f'CPU writing to main memory at address {address}: {data}')
        self.main_memory[address] = data

# adding idx associated to cache for implementing FIFO or other replacement methods, might change later
class CacheMemory:
    def __init__(self, size, idx = 0, main_memory_size = 128):
        self.size = size
        self.idx = idx
        self.main_memory = MainMemory(main_memory_size)
        self.data = [{'tag':None, 'data': None}] * self.size

    def retrieve_from_cache(self, address):
        if type(address) == int:
            address = '{0:08b'.format(address)
        for entry in self.data:
            if entry['tag'] == address and entry['data'] is not None:
                print(f"HIT: ", end = "")
                return entry

        print(f"MISS: ", end = "")
        return None

    def read_from_cache(self, address):
        data = None
        entry = self.retrieve_from_cache(address)
        if entry:
            print(f" - cache read: ")
            data = entry['data']
        else:
            data = self.main_memory.read_from_mainmemory(address)
            self.replace_add_entry(address, data)
        return data

    ## using a write-through policy for now
    def write_to_cache(self, address, data):
        if type(address) == int:
            address = '{0:08b}'.format(address)
        entry = self.retrieve_from_cache(address)
        if entry is not None:
            entry['data'] = data
        else:
            self.replace_add_entry(address, data)

        self.main_memory.write_into_mainmemory(address, data)

    def fifo_policy(self):
        index = self.idx
        self.idx += 1
        if self.idx == self.size:
            self.idx = 0
        return index

    def replace_add_entry(self, address, value):
        index = self.fifo_policy()
        self.data[index] = {'tag': address, 'data': value}







