import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def check_id_numbers(num_id, img_id):
    #The function recognizes the ID image and
    #distinguishes the ID number of the document.

    text_from_id = pytesseract.image_to_string(Image.open(img_id))
    str = ""
    for x in text_from_id:
        try:
            int(x)
            str += x
        except:
            continue
    #If it doesn't detect the ID number, it asks for another image
    if len(str) == 0:
        text = 'No number detected, please enter another image.'
        return False, text

    num_img_id = int(str)
    #It compares if the ID number is the same ID number that the user entry.
    #As the same way, it asks for another image
    if num_img_id != num_id:
        text = "Numbers don't match, please enter another image."
        return False, text
    return True, ''
