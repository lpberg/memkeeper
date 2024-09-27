from flask import Flask, jsonify, render_template, request, redirect
#from FileList import FileList
import sys
import os

# Helper Function
def flaskprint(str):
	print(str, file=sys.stderr)

# Create Flask Application
app = Flask(__name__)

# Create Route for Index Page
@app.route('/', methods=['GET'])
def render_index_page():
	return render_template("index.html")

# Create Route for Test Post (data communication)
@app.route('/test_post', methods=['POST'])
def test_post():
	response_data_dict = request.get_json()
	flaskprint(response_data_dict)
	return jsonify({'Flask Server':"POST Request was Successful"})

# Run Flask Application
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
