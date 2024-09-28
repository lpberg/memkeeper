import os
import sys
import uuid
import pickle

class MemoryCollection:
	def __init__(self,filename="outfile.pickle"):
		self.filename = filename
		self.readFromFile()
	def get(self,id):
		return(self.items[id])
	def add(self,memory):
		self.items[memory.get_id()] = memory
		self.writeToFile()
	def remove(self,id):
		self.items.pop(id)
		self.writeToFile()
	def get_size(self):
		return(len(self.items)) 
	def get_ids(self):
		return(self.items.keys())
	def readFromFile(self):
		if os.path.exists(self.filename):
			pickle_file = open(self.filename,'rb')
			self.items = pickle.load(pickle_file)
		else:
			self.items = {}
	def writeToFile(self):
		pickle_file = open(self.filename,'wb')
		pickle.dump(self.items,pickle_file)
		pickle_file.close()

class Memory():
	def __init__(self,data):
		self.id = str(uuid.uuid1())
		self.title = data["title"]
		self.desc = data["desc"]
	def get_id(self):
		return(self.id)
	def update(self,data):
		self.title = data["title"]
		self.desc = data["desc"]
	def get_data(self):
		return({"title":self.title,"desc":self.desc,"id":self.id})
