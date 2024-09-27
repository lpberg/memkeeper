import os
import sys
import uuid

class MemoryCollection:
	def __init__(self):
		self.items = {}
	def get(self,id):
		return(self.items[id])
	def add(self,memory):
		self.items[memory.get_id()] = memory
	def remove(self,id):
		self.items.pop(id)
	def get_ids(self):
		return(self.items.keys())

class Memory():
	def __init__(self,data):
		self.id = str(uuid.uuid4())
		self.title = data["title"]
		self.desc = data["desc"]
	def get_id(self):
		return(self.id)
	def update_data(self,data):
		self.title = data["title"]
		self.desc = data["desc"]
	def get_data(self):
		return({"title":self.title,"desc":self.desc,"id":self.id})
