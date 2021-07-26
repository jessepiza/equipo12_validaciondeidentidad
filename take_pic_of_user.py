from cv2 import *
# we define the function to access the user's camara and take two pictures


def take_pic_of_user(directory):
    # The camara is accessed
    vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    counter = 0
    # A loop is created to start taking the pictures of the user
    while True:
        next, frame = vc.read()
        cv2.imshow("WebCam", frame)
        # If the camara was not accessed the loop breaks
        if not next:
            break
        key = cv2.waitKey(1)
        # After two pictures taken the loop stops
        if counter == 2:
            break
        # The pictures are taken when the user presses the key indicated
        if key % 256 == 97:  # a
            # To avoid any mistakes the pictures taken are saved with the following names
            im_name = "image_{}.png".format(counter)
            cv2.imwrite(directory + '/' + im_name, frame)
            counter += 1

    # Finally, we release the operator capturing the video and delete all the windows that the program created.
    vc.release()
    cv2.destroyAllWindows()
