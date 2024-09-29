import os
import sys
import uuid
import json

class MemoryCollection:
	def __init__(self,memory_dir="memories"):
		self.memory_dir = memory_dir
		self.items = {}
		self.readFiles()
	def get(self,id):
		return(self.items[id])
	def add(self,memory):
		self.items[memory.get_id()] = memory
		self.writeFile(memory)
	def remove(self,id):
		self.items.pop(id)
	def get_size(self):
		return(len(self.items))
	def get_ids(self):
		return(self.items.keys())
	def writeFile(self,memory):
		json_object = json.dumps(memory.get_data(), indent=4)
		with open(self.memory_dir+"/"+memory.get_id()+".json", "w") as outfile:
			outfile.write(json_object)
	def writeFiles(self):
		for id, memory in self.items.items():
			self.writeFile(memory)
	def readFile(self,file):
		with open(self.memory_dir+"/"+file, 'r') as openfile:
			json_object = json.load(openfile)
		memory = Memory(json_object)
		self.add(memory)
	def readFiles(self):
		for file in os.listdir(self.memory_dir):
			if file.endswith('.json'):
				self.readFile(file)

class Memory():
	def __init__(self,data):
		self.id = str(uuid.uuid1())
		if "id" in data.keys():
			self.id = data["id"]
		self.title = data["title"]
		self.desc = data["desc"]
	def get_id(self):
		return(self.id)
	def update(self,data):
		self.title = data["title"]
		self.desc = data["desc"]
	def get_data(self):
		return({"title":self.title,"desc":self.desc,"id":self.id})
