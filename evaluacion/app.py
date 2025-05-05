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

@app.route('/evaluaciones', methods=['POST'])
def create_evaluacion():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO evaluaciones (rut_estudiante, semestre, asignatura, evaluacion) VALUES (%s, %s, %s, %s)"
    values = (data['rut_estudiante'], data['semestre'], data['asignatura'], data['evaluacion'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return jsonify({"message": "Evaluación creada"}), 201

@app.route('/evaluaciones', methods=['GET'])
def get_evaluaciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM evaluaciones"
    cursor.execute(query)
    evaluaciones = cursor.fetchall()
    cursor.close()
    return jsonify(evaluaciones), 200

@app.route('/evaluaciones/<rut_estudiante>', methods=['GET'])
def get_evaluacion(rut_estudiante):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM evaluaciones WHERE rut_estudiante=%s"
    values = (rut_estudiante,)
    cursor.execute(query, values)
    evaluacion = cursor.fetchone()
    cursor.close()
    if evaluacion:
        return jsonify(evaluacion), 200
    else:
        return jsonify({"message": "Evaluación no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
