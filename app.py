# Import / Load Libraries
from flask import Flask, jsonify, render_template, request, redirect
import sys
import os
# Import / Load Custom Written Libraries
from MemoryClasses import Memory, MemoryCollection

# Helper Function (to ensure print statements show up in python console)
def flaskprint(str):
	print(str, file=sys.stderr)

# Create MemoryCollection Object (helps read/write/manage Memory objects)
# "memories" is the name of a directory where files will be read/written
mc = MemoryCollection("memories")

# Create Flask Application
app = Flask(__name__)

# Create Route for Index Page
@app.route('/', methods=['GET'])
def render_index_page():
	# Respond to the GET request by rendering an html page
	ids_titles = mc.get_ids_titles()
	return render_template("index.html",ids_titles = ids_titles, num_items = mc.get_size())

# Create Route to Add a Memory
@app.route('/add', methods=['POST'])
def add():
	# data from the request is stored in request_data variable
	request_data = request.get_json()
	# request_data used an input parameters for new Memory object
	memory = Memory(request_data)
	# new memory object added to MemoryCollection object
	mc.add(memory)
	# Flask sends a response to request
	return jsonify({'Flask Server':"Memory "+memory.get_id()+" added"})

# Create Route to get Data for a Memory (via a Memory ID)
@app.route('/get', methods=['POST'])
def get():
	request_data = request.get_json()
	# the 'id' key from the request_data is used to lookup the Memory object, then the get_data() method returns the data from the object
	data = mc.get(request_data["id"]).get_data()
	return jsonify(data)

# Create Route to Update a Memory
@app.route('/update', methods=['POST'])
def update():
	request_data = request.get_json()
	# Look up Memory object in MemoryCollection object. Call Update with new set of values from the request
	mc.get(request_data["id"]).update({'title': request_data["title"], 'desc': request_data["desc"]})
	# Write the updated Memory to a file for long term storage
	mc.writeFile(mc.get(request_data["id"]))
	return jsonify({'Flask Server':request_data["id"]+" updated"})

# Create Route for Test Post (data communication)
@app.route('/test_post', methods=['POST'])
def test_post():
	response_data_dict = request.get_json()
	return jsonify({'Flask Server':"POST Test Request was Successful"})

# Run Flask Application on Port 5005
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
