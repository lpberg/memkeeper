import os
import sys
import uuid
import json
from datetime import datetime
import configparser

# Load configuration file
app_config = configparser.ConfigParser()
app_config.read('config.ini')

ACCEPTED_IMG_FORMATS = {".jpg",".jpeg",".png",".gif"}

class MemoryCollection:
	def __init__(self,memory_dir=app_config.get("app","memory_dir")):
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
		filename = os.path.join(self.memory_dir,str(memory.get_id())+".json")
		with open(filename, "w") as outfile:
			outfile.write(json.dumps(memory.get_data(), indent=4))
		outfile.close()
	def writeFiles(self):
		for id, memory in self.memories.items():
			self.writeFile(memory)
	def readFile(self,file):
		filename = os.path.join(self.memory_dir,file)
		infile = open(filename, 'r')
		json_object_from_file = json.load(infile)
		self.add(Memory(json_object_from_file))
		infile.close()
	def readFiles(self):
		for file in os.listdir(self.memory_dir):
			if file.endswith('.json'):
				self.readFile(file)

class Memory:
	def __init__(self,request_form,request_files=[]):
		# New memories need an id
		self.id = str(uuid.uuid1())
		# Memories loaded from file have an id already
		if "id" in request_form.keys():
			self.id = request_form["id"]
		self.upload_dir = os.path.join(app_config.get("app","upload_dir"),self.get_id())
		self.created_dt = datetime.now()
		# Memories loaded from file have created_dt already
		if "created_dt" in request_form.keys():
			self.created_dt = datetime.strptime(request_form["created_dt"], "%m/%d/%Y %H:%M:%S")
		self.dt = datetime.now()
		# Memories loadded from file have dt already
		if "dt" in request_form.keys():
			self.dt = datetime.strptime(request_form["dt"], "%m/%d/%Y %H:%M:%S")
		self.title = request_form["title"]
		self.desc = request_form["desc"]
		self.img_paths = []
		if (len(request_files)):
			self.add_images(request_files)
		self.refreshImgPaths()
	def add_images(self,request_files):
		if not os.path.exists(self.upload_dir):
			os.makedirs(self.upload_dir)
		for file_item in request_files:
			file = request_files[file_item]
			if file:
				if os.path.splitext(file.filename)[1] in ACCEPTED_IMG_FORMATS:
					file_path = os.path.join(self.upload_dir,file.filename)
					if not os.path.isfile(file_path):
						file.save(file_path)
		self.refreshImgPaths()
	def remove_image(self,path):
		if os.path.exists(path):
			os.remove(path)
		self.refreshImgPaths()
		if not os.path.exists(path):
			return True
		return False
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
	def get_imgPaths(self):
		return(self.img_paths)
	def refreshImgPaths(self):
		if os.path.exists(self.upload_dir):
			self.img_paths = [os.path.join(self.upload_dir,file) for file in os.listdir(self.upload_dir)]
	def update(self,data):
		if "title" in data.keys():
			self.title = data["title"]
		if "desc" in data.keys():
			self.desc = data["desc"]
		if "created_dt" in data.keys():
			self.created_dt = datetime.strptime(data["created_dt"], "%m/%d/%Y %H:%M:%S")
		if "dt" in data.keys():
			self.dt = datetime.strptime(data["dt"], "%m/%d/%Y %H:%M:%S")
		self.refreshImgPaths()
	def get_data(self):
		data = {
			"title":self.get_title(),
			"desc":self.get_desc(),
			"id":self.get_id(),
			"created_dt":self.get_created_dt_str(),
			"dt":self.get_dt_str(),
			"img_paths":self.get_imgPaths()
		}
		return(data)
