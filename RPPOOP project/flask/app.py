from flask import Flask, render_template, request
import face_recognition
import sqlite3
import os

app = Flask(__name__)

# Function to save uploaded image
def save_uploaded_image(file):
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    return file_path

# Function to compare faces
def compare_faces(reference_image, unknown_image):
    reference_encoding = face_recognition.face_encodings(reference_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([reference_encoding], unknown_encoding)
    return results[0]

# SQLite database connection
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create table for user data if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, college TEXT, adhaar TEXT, image_path TEXT)''')
conn.commit()

@app.route('/')
def registration_form():
    return render_template('main_registration.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    college = request.form['college']
    adhaar = request.form['adhaar']
    uploaded_image = request.files['image']

    # Save uploaded image
    image_path = save_uploaded_image(uploaded_image)

    # Compare faces
    reference_image = face_recognition.load_image_file("reference7.jpg.jpg")
    unknown_image = face_recognition.load_image_file(image_path)
    match = compare_faces(reference_image, unknown_image)

    # Insert data into database
    c.execute("INSERT INTO users (name, college, adhaar, image_path) VALUES (?, ?, ?, ?)",
              (name, college, adhaar, image_path))
    conn.commit()

    if match:
        return "Face matched successfully!"
    else:
        return "Face not recognized!"

if __name__ == '__main__':
    app.run(debug=True)
