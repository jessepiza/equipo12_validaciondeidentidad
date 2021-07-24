import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))

def image_cc(foto):
    img = cv2.imread(foto)
    text = pytesseract.image_to_string(img)
    str = ""
    for let in text:
        try:
            int(let)
            str += let
        except:
            continue
    return (int(str))
#
# img = cv2.imread("vale.jpeg")
# text = pytesseract.image_to_string(img)
#
# #img = cv2.imread("vale.jpeg")
# #print(text)
# str = ""
# for let in text:
#     try:
#         int(let)
#         str += let
#     except:
#         continue
#
# print(int(str))
