from flask import Flask, jsonify, request
from flask_cors import CORS
from database.database_functions import insert_my_time_to_db, fetch_all_records
app = Flask(__name__)
CORS(app)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask Web API!"

# Define an example API endpoint
@app.route('/api/example', methods=['GET'])
def example():
    return jsonify({"message": "This is an example endpoint"})

@app.route('/api/my_time_save', methods=['POST'])
def my_time_save():
    data = request.get_json()
    #if isinstance(data, dict):   
    #    json = jsonify(data)
    #    project_id = json['project_id']
    #    hours_worked = json['hours_worked']
    #    date = json['date']
    #    work_type = json['work_type']
    #    insert_my_time_to_db(project_id, hours_worked, date, work_type)
    #    return 200
    #else:
    #    return jsonify({"error": "Invalid input, expected a dictionary"}), 400
    return 200

if __name__ == '__main__':
    app.run(port=5001)
