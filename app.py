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

# Redirect root to view
@app.route('/', methods=['GET'])
def render_index_page():
	return redirect("/view")

# Create Route for Index Page
@app.route('/view', methods=['GET'])
def render_view_page():
	return render_template("view.html",ids_titles = mc.get_ids_titles(), ids_descriptions = mc.get_ids_descriptions)

# Create Route for Add Page
@app.route('/add', methods=['GET'])
def render_add_page():
    return render_template("add.html")

# Create Route for Add Page
@app.route('/view/<id>', methods=['GET'])
def render_view_single_page(id):
	id = request.view_args['id']
	data = mc.get(id).get_data()
	return render_template("view_single.html",title = data["title"],description = data["desc"])

# Create Route to Add a Memory
@app.route('/add_memory', methods=['POST'])
def add_memory():
	if request.method == "POST":
		request_data = request.get_json()
		memory = Memory(request_data)
		mc.add(memory)
		return jsonify({'Flask Server':"Memory "+memory.get_id()+" added"})

# Create Route to get Data for a Memory (via a Memory ID)
@app.route('/get_memory', methods=['POST'])
def get_memory():
	request_data = request.get_json()
	# the 'id' key from the request_data is used to lookup the Memory object, then the get_data() method returns the data from the object
	data = mc.get(request_data["id"]).get_data()
	return jsonify(data)

# Create Route to Update a Memory
@app.route('/update_memory', methods=['POST'])
def update_memeory():
	request_data = request.get_json()
	mc.get(request_data["id"]).update({'title': request_data["title"], 'desc': request_data["desc"]})
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
