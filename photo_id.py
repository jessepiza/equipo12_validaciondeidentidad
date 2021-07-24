import cv2
from PIL import Image
    
im = Image.open(r'vale.jpeg')
im.save(r'vale.png')

imagePath = r'imagen_0.png'
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)

image = cv2.imread(imagePath)
imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    imagegray,
    scaleFactor=1.5,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in faces:
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite('ceduladetect.png', image[y:y + h, x:x + w])

cv2.waitKey(0)
