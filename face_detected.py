import cv2
from PIL import Image
import os


def face_detected(directory):
    face_list = []
    for name_dir, dirs, files in os.walk(directory):
        for file in files:
            im = Image.open(name_dir + '/' + file)
            name_file = file[:file.find('.')]
            im.save(name_dir + '/' + name_file + '.png')
            if file.endswith(('.jpg', '.jpeg', '.gif', '.bmp', '.raw')):
                os.remove(name_dir + '/' + file)

            image_path = name_dir + '/' + name_file + '.png'
            casc_path = "haarcascade_frontalface_default.xml"

            # Create the haar cascade
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + casc_path)

            image = cv2.imread(image_path)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                image_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imwrite(name_dir + '/' + name_file + '.png', image[y:y + h, x:x + w])

            cv2.waitKey(0)
            face_list.append(name_dir + '/' + name_file + '.png')
    return face_list


dir_id = 'images_id'
dir_cam = 'images_cam'

print(face_detected(dir_id))
