from tkinter import *
from tkinter import messagebox

import cv2
from PIL import Image
from tkinter.filedialog import askopenfile
from check_id_numbers import check_id_numbers
from take_pic_of_user import take_pic_of_user
from face_detected import face_detected
from comparation import comparation

width = 1024
height = 650
dir_id = 'images_id'
dir_cam = 'images_cam'
font = "Playfair Display"
root = Tk()
root.resizable(0, 0)
# root = Frame(height=height, width=width, background="white")

# root.pack(padx=0, pady=0)
canvas = Canvas(root, width=width, height=height)


def window():
    clear()
    colorbk = '#CBCBD5'
    colorrect = '#02017F'
    canvas.create_rectangle(0, 0, width, height / 8, fill=colorrect)
    canvas.configure(background=colorbk)
    canvas.pack()
    # canvas.create_image(100, 100, image=logo, anchor=NW)
    context = "For validation purposes, please follow the next steps:"
    canvas.create_text(width / 16, 5 * height / 32, anchor=NW, text=context, font=(font, 20))
    first = "1.    Confirm your ID number. Remember not to use spaces nor dots."
    canvas.create_text(width / 16, height / 4, anchor=NW, text=first, font=(font, 18))
    id = "   Enter your ID number here: "
    canvas.create_text(3 * width / 32, 5 * height / 16, anchor=NW, text=id, font=(font, 15))
    field = Entry(canvas)
    canvas.create_window(width / 2, 41 * height / 128, anchor=N, window=field, width=width / 4)
    accept_button = Button(root, text="Accept", command=lambda: loading_process(field.get()), font=(font, 10),
                           background="white")
    canvas.create_window(11 * width / 16, 5 * height / 16, anchor=N, window=accept_button)


def loading_process(entry):
    second = '2.    Enter a clear image of your ID. Make sure your face and number ID are showing.'
    canvas.create_text(width / 16, 6 * height / 16, anchor=NW, text=second, font=(font, 18))
    upload_button = Button(root, text='Choose File', command=lambda: load_file(entry), font=(font, 15),
                           background="white")
    canvas.create_window(7 * width / 64, 7 * height / 16, anchor=NW, window=upload_button)


def clear():
    canvas.delete("all")


def load_file(entry):
    file_path = askopenfile(mode='r', filetypes=[('Image Files', ".jpeg .jpg .png .bmp")])
    im = Image.open(file_path.name)
    name_file = 'user_id.png'
    im.save(dir_id + '/' + name_file)
    if file_path is not None:
        pass
    img_id = dir_id + '/' + name_file
    num_id = entry
    check_id, text = check_id_numbers(int(num_id), img_id)
    if check_id:
        canvas.create_text(17 * width / 64, 7.2 * height / 16, anchor=NW, text="File uploaded successfully",
                           font=(font, 18), fill="green")
        third = '3.    For facial recognition purposes, please allow us access to your camera.'
        canvas.create_text(width / 16, 8.2 * height / 16, anchor=NW, text=third, font=(font, 18))
        accept_button = Button(root, text='Accept', command=lambda: validation_window(), font=(font, 15),
                               background="white")
        canvas.create_window(7 * width / 64, 9 * height / 16, anchor=NW, window=accept_button)
    else:
        messagebox.showerror("Error", text)


def validation_window():
    take_pic_of_user(dir_cam)
    images_id_list = face_detected(dir_id)
    images_cam_list = face_detected(dir_cam)
    for image in images_cam_list:
        user_pic = Image.open(image)
        user_id = Image.open(images_id_list[0])
        print(comparation(user_pic, user_id))




window()
root.mainloop()
