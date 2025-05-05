from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="microservicios"
    )
    return conn

@app.route('/estudiantes', methods=['POST'])
def create_student():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO estudiantes (rut, nombre_completo, edad, curso) VALUES (%s, %s, %s, %s)"
    values = (data['rut'], data['nombre_completo'], data['edad'], data['curso'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return jsonify({"message": "Estudiante creado"}), 201

@app.route('/estudiantes', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM estudiantes"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return jsonify(students), 200

@app.route('/estudiantes/<rut>', methods=['GET'])
def get_student(rut):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM estudiantes WHERE rut=%s"
    values = (rut,)
    cursor.execute(query, values)
    student = cursor.fetchone()
    cursor.close()
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"message": "Estudiante no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
