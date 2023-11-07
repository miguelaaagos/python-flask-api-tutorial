# add the jsonify method to your Flask import
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

# suppose you have your data in the variable named some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # and then you can return it to the front end in the response body like this
    return json_text


@app.route('/todos', methods=['GET'])
def get_todos():
   json_todos = jsonify(todos)

   return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    
    # Add the request_body (a dictionary) to the todos list
    todos.append(request_body)
    
    # Return the updated list todos to the front end, jsonify the response
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    print("This is the position to delete: ",position)
    if 0 <= position < len(todos):
        # Remove the task at the specified position
        del todos[position]
        
        # Return the updated list todos to the front end, jsonify the response
        return jsonify(todos)
    else:
        # Return a response indicating that the specified position is out of range
        return "Position out of range", 400  # You can choose an appropriate status code



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)