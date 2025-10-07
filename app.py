from flask import Flask, jsonify, request
from deep_translator import GoogleTranslator
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    return psycopg2.connect(
        host="YOUR_DB_HOST",
        database="YOUR_DB_NAME",
        user="YOUR_DB_USER",
        password="YOUR_DB_PASSWORD"
    )

# Function to translate text to Tamil
def translate_to_tamil(text):
    try:
        if not text:
            return text
        return GoogleTranslator(source='auto', target='ta').translate(text)
    except Exception as e:
        print("Translation Error:", e)
        return text

# Fetch and translate users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in rows:
        for key in row:
            if isinstance(row[key], str):
                row[key] = translate_to_tamil(row[key])

    return jsonify(rows)

# Fetch and translate appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in rows:
        for key in row:
            if isinstance(row[key], str):
                row[key] = translate_to_tamil(row[key])

    return jsonify(rows)

# Fetch and translate doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in rows:
        for key in row:
            if isinstance(row[key], str):
                row[key] = translate_to_tamil(row[key])

    return jsonify(rows)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
