import sqlite3

@app.route('/api', methods=['GET'])
def get_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
    ''')

    # Retrieve data from the database
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert the data to a JSON response
    data = [{'id': row[0], 'message': row[1]} for row in rows]
    return jsonify(data)
#

@app.route('/api', methods=['POST'])
def post_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Insert data into the database
    data = request.get_json()
    message = data['message']
    cursor.execute('INSERT INTO data (message) VALUES (?)', (message,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Return a success response
    return jsonify({'message': 'Data received and inserted