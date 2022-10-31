# cpu-simulator

I made a rudimentary CPU simulator. Below is some description of the parts of the code and a short description of how the code works. 

#### Classes ####

There are four main classes in the current CPU simulator. Namely:

  - Main Memory class
  - Cache Memory class
  - CPU class 
  
The Main Memory class consists of a dictionary with keys binary numbers representing addresses and comes with basic reading, writing, and fetching methods which simulate reading, writing, and fetching data from the main memory of the CPU. Likewise the Cache Memory Class has methods to read, write, and fetch from cache memory. One idiosyncracy of how I wrote the Cache Memory class is that it contains an instance of a Main Memory object. Within the Cache Memory class, I also implemented a FIFO replacement and write-through method for interacting with the main memory. In the future I would like to implement more sophisticated replacement and write methods. 

The CPU class currently only has basic methods pertaining to reading and writing to registers and reading basic instructions such as `ADD`, `ADDI`, `J`, and and `CACHE`. Additionally, there is a method designed to parse instructions from instruction input files. 

#### Possible improvements ####

There are several things I would like to do to update this project and make a more detailed CPU simulator. These include the following:

  - Create a Parent Memory class and make Main Memory and Cache Memory children classes of it. Additionally create a separate Memory Bus class which more accurately simulates the interaction between these two components, 
  - In the file cpu-components.py, create a class for the ALU which implements logic gates, half-adder, and full-adders, 
  - Create an Assemblor class which simulates the assemblor in the CPU translating between assembly language and machine language. Related to this, implement a ISA (most likely MIPS32). 
  - Implement different kinds of processing parallelism (e.g. pipelining), 
  - Simulate a GPU.
  
 All of these will require a bit more research on my part. Hopefully I will be able to implement some of these soon. 
