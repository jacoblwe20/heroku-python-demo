import os
from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Try New Coffee Place',
        'description': 'Across from the Mission Inn heard they have a mean expresso', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Finish up README.md jacoblwe20/marrow',
        'description': 'There still need to be more documentation about setup', 
        'done': True
    }
];

@app.route('/api/v0/tasks.json', methods = ['GET'])
def get_tasks():
	return jsonify( { 'tasks' : tasks } )


@app.route('/')
def not_found():
    return '404 Not Found try <a href="/api/v0/tasks.json">/api/v0/tasks.json</a>';

if __name__ == '__main__':
    app.run(port= int(os.getenv('PORT', 5000)))
