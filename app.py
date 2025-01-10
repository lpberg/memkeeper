# Import / Load Libraries
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
import uuid
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

# Set upload directory
# TODO: enforce image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = './static/uploads/images'

# Redirect root to view
@app.route('/', methods=['GET'])
def render_index_page():
	return render_template("view.html",memories = mc.get_data())

# Create Route for Index Page
@app.route('/view', methods=['GET'])
def render_view_page():
	return render_template("view.html",memories = mc.get_data())

# Helper function that creates directories and saves images from add memory function
def process_images(request_files,id):
	img_paths = []
	if 'file1' in request_files:
		if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],str(id))):
			os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'],str(id)))
		file = request_files['file1']
		if file:
			path = os.path.join(app.config['UPLOAD_FOLDER'],str(id),file.filename)
			file.save(path)
			img_paths.append(path)
	return img_paths

# Create Route to Add a Memory
@app.route('/add_memory', methods=['POST'])
def add_memory():
	if request.method == "POST":
		request_data = {}
		request_data["id"] = str(uuid.uuid1())
		request_data["title"] = request.form["title"]
		request_data["desc"] = request.form["desc"]
		request_data["img_paths"] = process_images(request.files,request_data["id"])
		memory = Memory(request_data)
		mc.add(memory)
		return jsonify({'Flask Server':"Memory added"})

# Create Route to get Data for a Memory (via a Memory ID)
@app.route('/get_memory', methods=['POST'])
def get_memory():
	request_data = request.get_json()
	data = mc.get(request_data["id"]).get_data()
	return jsonify(data)

# Create Route to Update a Memory
# TODO - redo update call using new data structure
@app.route('/update_memory', methods=['POST'])
def update_memeory():
	request_data = request.get_json()
	memory = mc.get(request_data["id"])
	memory.update(request_data)
	mc.writeFile(memory)
	return jsonify({'Flask Server':request_data["id"]+" updated"})

# Run Flask Application on Port 5005
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
