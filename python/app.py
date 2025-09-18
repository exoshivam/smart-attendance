from flask import Flask, request, jsonify
import face_recognition
import numpy as np
import os
import pickle

app = Flask(__name__)
ENCODINGS_PATH = 'encodings.pkl'

# Load or initialize encodings
if os.path.exists(ENCODINGS_PATH):
    with open(ENCODINGS_PATH, 'rb') as f:
        encodings_db = pickle.load(f)
else:
    encodings_db = {}

@app.route('/register', methods=['POST'])
def register():
    student_id = request.form.get('student_id')
    if 'photo' not in request.files or not student_id:
        return jsonify({'error': 'Missing photo or student_id'}), 400
    photo = request.files['photo']
    img = face_recognition.load_image_file(photo)
    encodings = face_recognition.face_encodings(img)
    if not encodings:
        return jsonify({'error': 'No face found'}), 400
    encodings_db[student_id] = encodings[0]
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(encodings_db, f)
    return jsonify({'success': True, 'student_id': student_id})

@app.route('/identify', methods=['POST'])
def identify():
    if 'photo' not in request.files:
        return jsonify({'error': 'Missing photo'}), 400
    photo = request.files['photo']
    img = face_recognition.load_image_file(photo)
    encodings = face_recognition.face_encodings(img)
    if not encodings:
        return jsonify({'error': 'No face found'}), 400
    unknown_encoding = encodings[0]
    for student_id, known_encoding in encodings_db.items():
        match = face_recognition.compare_faces([known_encoding], unknown_encoding)[0]
        if match:
            return jsonify({'success': True, 'student_id': student_id})
    return jsonify({'success': False, 'student_id': None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
