from flask import Flask, jsonify, render_template, request, redirect
from MemoryClasses import Memory, MemoryCollection
import sys
import os

# Helper Function
def flaskprint(str):
	print(str, file=sys.stderr)

mc = MemoryCollection("data.flask.pickle")

# Create Flask Application
app = Flask(__name__)

# Create Route for Index Page
@app.route('/', methods=['GET'])
def render_index_page():
	return render_template("index.html",num_items = mc.get_size())

# Create Route to add a Memory
@app.route('/add', methods=['POST'])
def add():
	request_data = request.get_json()
	memory = Memory(request_data)
	mc.add(memory)
	return jsonify({'Flask Server':"Memory "+memory.get_id()+" added"})

# Create Route to get Data for a Memory
@app.route('/get', methods=['POST'])
def get():
	request_data = request.get_json()
	data = mc.get(request_data["id"]).get_data()
	return jsonify(data)

# Create Route to update a Memory
@app.route('/update', methods=['POST'])
def update():
	request_data = request.get_json()
	mc.get(request_data["id"]).update({'title': request_data["title"], 'desc': request_data["desc"]})
	mc.writeToFile()
	return jsonify({'Flask Server':request_data["id"]+" updated"})

# Create Route for Test Post (data communication)
@app.route('/test_post', methods=['POST'])
def test_post():
	response_data_dict = request.get_json()
	return jsonify({'Flask Server':"POST Test Request was Successful"})

# Run Flask Application
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
