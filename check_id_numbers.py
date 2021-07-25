import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def check_id_numbers(num_id, img_id):
    text_from_id = pytesseract.image_to_string(img_id)
    str = ""
    for x in text_from_id:
        try:
            int(x)
            str += x
        except:
            continue

    if len(str) == 0:
        text = 'No number detected, please enter another image.'
        return False, text

    num_img_id = int(str)
    print(num_img_id)

    if num_img_id != num_id:
        text = "Numbers don't match, please enter another image."
        return False, text
    return True, ''
