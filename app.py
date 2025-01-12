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
mc = MemoryCollection("memories")

# Create Flask Application
app = Flask(__name__)

# Set upload directory - flask requires use of static dir
app.config['UPLOAD_FOLDER'] = './static/uploads/images'

# Redirect root to view
@app.route('/', methods=['GET'])
def render_index_page():
	return render_template("view.html",memories = mc.get_data())

# Create Route for Index Page
@app.route('/view', methods=['GET'])
def render_view_page():
	return render_template("view.html",memories = mc.get_data())

# Create Route to Add a Memory
@app.route('/memory/add', methods=['POST'])
def add_memory():
	if request.method == "POST":
		memory = Memory(request.form,request.files,app.config['UPLOAD_FOLDER'])
		mc.add(memory)
		return jsonify({'Flask Server':"Memory added"})

# Create Route to get Data for a Memory (via a Memory ID)
@app.route('/memory/get', methods=['POST'])
def get_memory():
	request_data = request.get_json()
	data = mc.get(request_data["id"]).get_data()
	return jsonify(data)

# Create Route to Update a Memory
@app.route('/memory/update', methods=['POST'])
def update_memory():
	request_data = request.get_json()
	memory = mc.get(request_data["id"])
	memory.update(request_data)
	mc.writeFile(memory)
	return jsonify({'Flask Server':request_data["id"]+" updated"})

# Create Route to Add Images to Existing Memory
@app.route('/image/add', methods = ['POST'])
def add_images_to_memory():
	if request.method == 'POST':
		memory = mc.get(request.form["id"])
		added_images = memory.add_images(request.files)
	return jsonify({"img_paths":added_images})

# Create Route to Remove Image from Existing Memory
@app.route("/image/remove", methods = ['POST'])
def remove_image_from_memory():
	if request.method == 'POST':
		memory = mc.get(request.form["id"])
		removal_successful = memory.remove_image(request.form["img_path"])
	return jsonify({request.form["img_path"]:removal_successful})

# Run Flask Application on Port 5005
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
