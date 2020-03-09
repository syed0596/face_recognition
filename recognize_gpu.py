import face_recognition
import cv2


img = cv2.imread('degeners.jpg')
unknown_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face_locations = face_recognition.face_locations(unknown_image,model='cnn')
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    img = cv2.rectangle(img,(left,top),(right,bottom),(255,0,0),2)
    roi_gray = unknown_image[bottom,right]
    roi_color = img[bottom, right]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
