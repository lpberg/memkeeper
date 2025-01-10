import os
import sys
import uuid
import json
from datetime import datetime

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
	def get_data(self):
		data = {}
		for id, memory in self.memories.items():
			data[id] = memory.get_data()
		return(data)
	def writeFile(self,memory):
		filename = self.memory_dir+"/"+str(memory.get_id())+".json"
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
		self.created_dt = datetime.now()
		self.dt = datetime.now()
		self.img_paths = []
		if "id" in data.keys():
			self.id = data["id"]
		if "created_dt" in data.keys():
			self.created_dt = datetime.strptime(data["created_dt"], "%m/%d/%Y %H:%M:%S")
		if "dt" in data.keys():
			self.dt = datetime.strptime(data["dt"], "%m/%d/%Y %H:%M:%S")
		if "img_paths" in data.keys():
			if len(data["img_paths"])>0:
				for path in data["img_paths"]:
					if path not in self.img_paths:
						self.img_paths.append(path)
		self.title = data["title"]
		self.desc = data["desc"]
	def get_id(self):
		return(self.id)
	def get_title(self):
		return(self.title)
	def get_desc(self):
		return(self.desc)
	def get_dt(self):
		return(self.dt)
	def get_dt_str(self):
		return(self.dt.strftime("%m/%d/%Y %H:%M:%S"))
	def get_created_dt(self):
		return(self.created_dt)
	def get_created_dt_str(self):
		return(self.created_dt.strftime("%m/%d/%Y %H:%M:%S"))
	def update(self,data):
		if "title" in data.keys():
			self.title = data["title"]
		if "desc" in data.keys():
			self.desc = data["desc"]
		if "created_dt" in data.keys():
			self.created_dt = datetime.strptime(data["created_dt"], "%m/%d/%Y %H:%M:%S")
		if "dt" in data.keys():
			self.dt = datetime.strptime(data["dt"], "%m/%d/%Y %H:%M:%S")
		if "img_paths" in data.keys():
			# TODO: Consider overwriting list vs conditional appending
			self.img_paths = data["img_paths"]
	def get_data(self):
		return({"title":self.title,"desc":self.desc,"id":self.id,"created_dt":self.get_created_dt_str(),"dt":self.get_dt_str(),"img_paths":self.img_paths})
