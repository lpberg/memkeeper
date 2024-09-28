from MemoryClasses import Memory, MemoryCollection

# Create Memory Collection object
mc = MemoryCollection("myoutfile.pickle")

# Create Memories and add to Memory Collection object
mc.add(Memory({"title":"Memory A","desc":"This is a description for Memory A"}))
mc.add(Memory({"title":"Memory B","desc":"This is a description for Memory B"}))
mc.add(Memory({"title":"Memory A","desc":"This is a description for Memory A"}))

# Grab the first key in the MemoryCollection
#sample_key = list(mc.get_ids())[0]
#print("Sample Key: "+sample_key)

# Update the Memory (stored in that key)
#mc.get(sample_key).update_data({"title":"A New Title for Memory","desc":"A New Description for Memory"})
#print(mc.get(sample_key).get_data())

# Print out all keys and data
for key in list(mc.get_ids()):
	print(mc.get(key).get_data())
