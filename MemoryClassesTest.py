from MemoryClasses import Memory, MemoryCollection

# Create Memory Collection object
mc = MemoryCollection("memories")

# Create Memories and add to Memory Collection object
new_memory = Memory({"title":"Memory A","desc":"This is a description for Memory A"})
mc.add(new_memory)

# Get size of Memory Collection
num_memories = mc.get_size()
print(f"There are {num_memories} memories in this collection.")

# Get and print ids in the Memeory Collection
ids = mc.get_ids()
#[print(id) for id in ids]

# Get data from a Memory
memory_data = mc.get("example").get_data()
print(memory_data)

# Update a Memory 
memory = mc.get('example')
print(f"Before update: {memory.get_data()}")
memory.update({'title':"a brand new title","desc":"a brand new desc"})
print(f"After update: {mc.get('example').get_data()}")
