from flask import Flask, jsonify, render_template, request, redirect
#from FileList import FileList
import sys
import os

def flaskprint(str):
	print(str, file=sys.stderr)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return redirect("/platform/movies")

@app.route('/platform/<system>', methods=['GET'])
def platform(system):
	system = request.view_args['system']
	return render_template("index.html",system=system,systems=systems)

@app.route('/<system>/add', methods=['POST'])
def add(system):
	title = request.form['title']
	system = request.view_args['system']
	c[system].add(title)
	return jsonify({'output':"Added: " + title})

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,threaded=True,port=5005)
