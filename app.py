from flask import Flask, jsonify, request
from flask_cors import CORS
from database.database_functions import insert_my_time_to_db, fetch_all_records
app = Flask(__name__)
CORS(app)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask Web API!"

@app.route('/api/my_time_save', methods=['POST'])
def my_time_save():
    data = request.get_json()
    if isinstance(data, dict):
        project_id = data['project_id']
        hours_worked = data['hours_worked']
        date = data['date']
        work_type = data['work_type']
        userid = 'user_1'
        insert_my_time_to_db(project_id, hours_worked, date, work_type, userid)
        
        all_records = fetch_all_records(userid)
        response = {
            "data": data,
            "all_records": all_records
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid input, expected a dictionary"}), 400
    
@app.route('/api/get_records_by_userid', methods=['GET'])
def get_records_by_userid():
    data = request.get_json()
    if isinstance(data, dict):
        userid = data['userid']       
        all_records = fetch_all_records(userid)
        response = {
            "all_records": all_records
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid input, expected a dictionary"}), 400

if __name__ == '__main__':
    app.run(port=5001)
