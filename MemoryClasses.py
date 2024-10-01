import os
import sys
import uuid
import json

class MemoryCollection:
	def __init__(self,memory_dir="memories"):
		self.memory_dir = memory_dir
		self.memories = {}
		self.readFiles()
	def get(self,id):
		return(self.memories[id])
	def add(self,memory):
		self.memories[memory.get_id()] = memory
		self.writeFile(memory)
	def remove(self,id):
		self.memories.pop(id)
	def get_size(self):
		return(len(self.memories))
	def get_ids(self):
		return(self.memories.keys())
	def writeFile(self,memory):
		filename = self.memory_dir+"/"+memory.get_id()+".json"
		with open(filename, "w") as outfile:
			outfile.write(json.dumps(memory.get_data(), indent=4))
		outfile.close()
	def writeFiles(self):
		for id, memory in self.memories.items():
			self.writeFile(memory)
	def readFile(self,file):
		filename = self.memory_dir+"/"+file
		infile = open(filename, 'r')
		json_object_from_file = json.load(infile)
		self.add(Memory(json_object_from_file))
		infile.close()
	def readFiles(self):
		for file in os.listdir(self.memory_dir):
			if file.endswith('.json'):
				self.readFile(file)

class Memory:
	def __init__(self,data):
		self.id = str(uuid.uuid1())
		if "id" in data.keys():
			self.id = data["id"]
		self.title = data["title"]
		self.desc = data["desc"]
	def get_id(self):
		return(self.id)
	def get_title(self):
		return(self.title)
	def get_desc(self):
		return(self.desc)
	def update(self,data):
		self.title = data["title"]
		self.desc = data["desc"]
	def get_data(self):
		return({"title":self.title,"desc":self.desc,"id":self.id})
