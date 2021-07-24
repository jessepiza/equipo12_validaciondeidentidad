import cv2
import numpy as np
from cv2 import *


def take_pic_from_user():

    vc = cv2.VideoCapture(0)
    counter = 0
    while True:
        next, frame = vc.read()
        cv2.imshow("WebCam", frame)

        if not next:
            break
        key = cv2.waitKey(100)
        if key & 0xFF == ord('q'):
            break
        if key % 256 == 97:  # a
            im_name = "imagen_{}.png".format(counter)
            cv2.imwrite(im_name, frame)
            print("{} written!".format(im_name))
            counter += 1

    vc.release()
    cv2.destroyAllWindows()


take_pic_from_user()

#grabar y guardar un video

#
#
# idk = cv2.VideoWriter_fourcc(*'MP4V')
# out = cv2.VideoWriter('video.mp4', idk, 20.0, (640, 480))
#
# while vc.isOpened():
#     next, frame = vc.read()
#     if next == True:
#         cv2.imshow('WebCam', frame)
#         out.write(frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# vc.release()
# out.release()
# cv2.destroyAllWindows()

#toma la foto sin funcion

# vc = cv2.VideoCapture(0)
#
# counter = 0
# while True:
#     net, frame = vc.read()
#     cv2.imshow("WebCam", frame)
#
#     if not net:
#         break
#     key = cv2.waitKey(1)
#     if key & 0xFF == ord('q'):
#         break
#     if key % 256 == 97: #a
#         im_name = "imagen_{}.png".format(counter)
#         cv2.imwrite(im_name, frame)
#         print("{} written!".format(im_name))
#         counter += 1
#
# vc.release()
# cv2.destroyAllWindows()




# no es lo que necesito

# while True:
#     next, frame = vc.read()
#     cv2.imshow("webcam", frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# vc.release()
# vc.VideoWriter()