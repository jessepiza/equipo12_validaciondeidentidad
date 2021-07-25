from cv2 import *


def take_pic_of_user(directory):
    vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    counter = 0
    while True:
        next, frame = vc.read()
        cv2.imshow("WebCam", frame)

        if not next:
            break
        key = cv2.waitKey(1)
        if counter==2:
            break
        if key % 256 == 97:  # a
            im_name = "image_{}.png".format(counter)
            cv2.imwrite(directory + '/' + im_name, frame)
            counter += 1

    vc.release()
    cv2.destroyAllWindows()
