import face_recognition

while True:
    picture_of_me = face_recognition.load_image_file("reference7.jpg.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]