import face_recognition

known_faces =[]
i=1
while i<=12:
    picture_of_me = face_recognition.load_image_file(r"C:\Users\aryaw\OneDrive\Desktop\Arya test programs\database\image"+str(i)+".jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    i=i+1
    known_faces.append(my_face_encoding)

unknown_picture = face_recognition.load_image_file(r"C:\Users\aryaw\OneDrive\Pictures\Camera Roll\WIN_20240404_14_03_12_Pro.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

j=0

while j<=11:
        results = face_recognition.compare_faces([known_faces[j]], unknown_face_encoding, tolerance=0.40)
        if results[0]== True:
            print("Image found! It's a picture from image"+str(j+1))
            break
        elif j==12:
             print("no matches found")
        j=j+1
             
            

