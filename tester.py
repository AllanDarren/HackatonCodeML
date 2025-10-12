import cv2
import face_recognition

# Load and convert images (example files; replace with your own)
imgLoaded = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgLoaded = cv2.cvtColor(imgLoaded, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Find face locations and encodings
faceLoc = face_recognition.face_locations(imgLoaded)[0]
encodeImg = face_recognition.face_encodings(imgLoaded)[0]
cv2.rectangle(imgLoaded, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# Compare
results = face_recognition.compare_faces([encodeImg], encodeTest)
faceDis = face_recognition.face_distance([encodeImg], encodeTest)
print('Match:', results, 'Distance:', faceDis)

cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}',
            (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Elon', imgLoaded)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)
cv2.destroyAllWindows()
