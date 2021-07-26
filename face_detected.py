import cv2
from PIL import Image
import os


def face_detected(directory):
    # Function that detects the images of a folder and returns a list with the faces of images path
    face_list = []
    for name_dir, dirs, files in os.walk(directory):
        for file in files:
            # Iteration in the files of the selected folder
            im = Image.open(name_dir + '/' + file)  # Open Image
            name_file = file[:file.find('.')]  # Image without the format
            im.save(name_dir + '/' + name_file + '.png')  # Change format of image
            if file.endswith(('.jpg', '.jpeg', '.gif', '.bmp', '.raw')):
                os.remove(name_dir + '/' + file)

            # Path of new image face
            image_path = name_dir + '/' + name_file + '.png'
            casc_path = "haarcascade_frontalface_default.xml"

            # Create the haar cascade
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + casc_path)

            # Origin image in gray
            image = cv2.imread(image_path)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(
                image_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Write the faces in the folder
            for (x, y, w, h) in faces:
                cv2.imwrite(name_dir + '/' + name_file + '.png', image[y:y + h, x:x + w])

            cv2.waitKey(0)

            # Insert images path in the folder
            face_list.append(name_dir + '/' + name_file + '.png')
    return face_list
