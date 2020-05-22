from PIL import Image
import face_recognition

image = face_recognition.load_image_file('photo2.jpg')
face_locations = face_recognition.face_locations(image)

size = 300, 300
baseWidth = 300

for face_location in face_locations:
	top, right, bottom, left = face_location
	face_image = image[top:bottom, left:right]
	
	pilImage = Image.fromarray(face_image)
	pilImage.show()
	