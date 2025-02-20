import pyodbc
from datetime import datetime

def insert_my_time_to_db(project_id: str, hours_worked: str, date:str, work_type: str, userid: str):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    connection = initiate_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO [dbo].[MyTimeTracking] (date, hours, project_id, work_type, userid)
        VALUES (?, ?, ?, ?, ?)
    """, date_obj, hours_worked, project_id, work_type, userid)
    connection.commit()
    cursor.close()
    close_connection(connection)

def fetch_all_records(userid: str):
    records = []
    connection = initiate_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT date, hours, project_id, work_type, userid FROM [dbo].[MyTimeTracking] WHERE userid = ?", (userid,))
    for row in cursor.fetchall():
        records.append({
            'date': row.date,
            'hours': row.hours,
            'project_id': row.project_id,
            'work_type': row.work_type,
            'userid': row.userid
        })
    cursor.close()
    close_connection(connection)
    return records

def initiate_connection():
    # Replace these values with your database details
    server = 'localhost'
    database = 'PythonDatabase'
    username = 'power_user'
    password = 'password1234'

    # Connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # Establish a connection
        connection = pyodbc.connect(connection_string)
        print("Connection successful!")
        return connection

    except pyodbc.Error as e:
        print("Error: ", e)

def close_connection(connection):
    # Close the connection
    if connection:
        connection.close()