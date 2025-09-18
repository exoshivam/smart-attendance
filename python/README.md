# Python Facial Recognition API

This project provides a Flask-based API for facial recognition. It allows registering student faces and identifying students from uploaded photos using the `face_recognition` library.

## Features

- Register student faces by uploading a photo and student ID
- Identify students from uploaded photos
- Stores facial encodings for matching

## Endpoints

- `/register` (POST): Register a student face
- `/identify` (POST): Identify a student from a photo

## Setup

1. Install dependencies: `pip install flask face_recognition numpy`
2. Run the server: `python app.py`

## Usage

- Integrate with your Node.js backend to send student photos for registration and identification.

## Note

- Facial encodings are stored in a file/database for demonstration. For production, use a proper database.
