from MemoryClasses import Memory, MemoryCollection
import os
import unittest

class TestMemoryClass(unittest.TestCase):
	def setUp(self):
		self.memory_data = {"id":"example_id","title":"Test Memory","desc":"This is a description for a Test Memory"}
		self.memory = Memory(self.memory_data)
	def test_get_id(self):
		self.assertEqual(self.memory.get_id(), 'example_id')
	def test_get_title(self):
		self.assertEqual(self.memory.get_title(),'Test Memory')
	def test_get_desc(self):
		self.assertEqual(self.memory.get_desc(),'This is a description for a Test Memory')
	def test_update(self):
		self.memory.update({"title":"Updated Test Memory Title","desc":"This is a description for a Test Memory"})
		self.assertEqual(self.memory.get_title(),"Updated Test Memory Title")
	def test_get_data(self):
		self.assertEqual(self.memory.get_data(),self.memory_data)

class TestMemoryCollectionClass(unittest.TestCase):
	def setUp(self):
		self.mc = MemoryCollection("memories")
		self.dir_size = len(os.listdir('memories'))
	def test_get_size(self):
		self.assertEqual(self.dir_size, self.mc.get_size())
	def test_add(self):
		memory = Memory({"id":"example_id","title":"Test Memory","desc":"This is a description for a Test Memory"})
		self.mc.add(memory)
		self.assertTrue("example_id" in self.mc.get_ids())
	def test_remove(self):
		memory = Memory({"id":"example_id","title":"Test Memory","desc":"This is a description for a Test Memory"})
		self.mc.add(memory)
		self.mc.remove('example_id')
		self.assertFalse("example_id" in self.mc.get_ids())

# TODO: Add other Class Functions for MemoryCollection
# readFile
# writeFile
# get_ids
# get

if __name__ == '__main__':
    unittest.main()
