import face_recognition
from PIL import Image, ImageDraw

unknown_image = face_recognition.load_image_file("degeners.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image, model='cnn')
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

# Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))

    # Draw a label with a name below the face
    draw.rectangle(((left, bottom), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
    


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()
