from MemoryClasses import Memory, MemoryCollection

# Create Memory Collection object
mc = MemoryCollection("memories")
# Create Memories and add to Memory Collection object
mc.add(Memory({"title":"Memory A","desc":"This is a description for Memory A"}))
mc.add(Memory({"title":"Memory B","desc":"This is a description for Memory B"}))
mc.add(Memory({"title":"Memory A","desc":"This is a description for Memory A"}))

print(f"There are {len(mc.get_ids())} memories in this collection.")

# Print out all keys and data
#for key in list(mc.get_ids()):
#	print(mc.get(key).get_data())
