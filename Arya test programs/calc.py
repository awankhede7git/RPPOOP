import face_recognition
known_faces =[]
i=1
while i<=12:
    picture_of_me = face_recognition.load_image_file(r"C:\Users\aryaw\OneDrive\Desktop\Arya test programs\database\image"+str(i)+".jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    i=i+1
    known_faces.append(my_face_encoding)
