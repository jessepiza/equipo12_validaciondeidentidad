import numpy as np
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))
from cv2 import *


def check_id_numbers(num_id, img_id):
    text_from_id = pytesseract.image_to_string(img_id)
    str = ""
    #print(text_from_id)
    for x in text_from_id:
        try:
            int(x)
            str += x
        except:
            continue

    if len(str) == 0:
        print('No se detecto ningun número, ingrese otra imagen.')
        return False

    num_img_id = int(str)
    #print(num_img_id)

    if num_img_id != num_id:
        print('Los números no coinciden, ingrese otra imagen.')
        return False

    return True

##################
### Main code
##################

vc = cv2.VideoCapture(0)
counter = 0
while True:
    next, frame = vc.read()
    cv2.imshow("WebCam", frame)

    if not next:
        break
    key = cv2.waitKey(250)
    if key & 0xFF == ord('q'):
        break
    if key % 256 == 97:  # a
        im_name = "imagen_{}.png".format(counter)
        cv2.imwrite(im_name, frame)
        print("{} written!".format(im_name))
        counter += 1

vc.release()
cv2.destroyAllWindows()

num_id = int(input('Ingrese cedula: '))
img_id = cv2.imread("cedula4.jpeg")

# Check if the id numbers match

test_num_id = check_id_numbers(num_id, img_id)

# Read pic of user

pic_from_user = cv2.imread("imagen_{}.png".format(counter))

