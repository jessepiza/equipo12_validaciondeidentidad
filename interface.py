from tkinter import *
from tkinter import messagebox
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
count_fail_id = 0
count_fail_cap = 0
colorbk = '#CBCBD5'
colorrect = '#02017F'


def window():
    global count_fail_id, count_fail_cap
    count_fail_id, count_fail_cap = 0, 0
    clear()
    canvas.create_rectangle(0, 0, width, height / 8, fill=colorrect)
    canvas.configure(background=colorbk)
    canvas.pack(fill="both", expand=True)

    #panel.pack(side="bottom", fill="both", expand="yes")
    context = "For validation purposes, please follow the next steps:"
    canvas.create_text(width / 16, 5 * height / 32, anchor=NW, text=context, font=(font, 20))
    first = "1.    Confirm your ID number. Remember not to use spaces nor dots."
    canvas.create_text(width / 16, height / 4, anchor=NW, text=first, font=(font, 18))
    id = "   Enter your ID number here: "
    canvas.create_text(3 * width / 32, 5 * height / 16, anchor=NW, text=id, font=(font, 15))
    field = Entry(canvas)
    canvas.create_window(width / 2, 41 * height / 128, anchor=N, window=field, width=width / 4)
    accept_button = Button(root, text="Accept", command=lambda: loading_process(field, accept_button), font=(font, 10),
                           background="white")
    canvas.create_window(11 * width / 16, 5 * height / 16, anchor=N, window=accept_button)


def loading_process(field, accept_button):
    second = '2.    Enter a clear image of your ID. Make sure your face and number ID are showing.'
    canvas.create_text(width / 16, 6 * height / 16, anchor=NW, text=second, font=(font, 18))
    upload_button = Button(root, text='Choose File', command=lambda: load_file(field, accept_button, upload_button),
                           font=(font, 15),
                           background="white")
    canvas.create_window(7 * width / 64, 7 * height / 16, anchor=NW, window=upload_button)


def clear():
    canvas.delete("all")


def load_file(field, accept_butt, upload_button):
    global count_fail_id
    entry = field.get()
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
        field.config(state='disabled')
        accept_butt.config(state='disabled')
        upload_button.config(state='disabled')
        canvas.create_text(17 * width / 64, 7.2 * height / 16, anchor=NW, text="File uploaded successfully",
                           font=(font, 18), fill="green")
        third = r'3.    For facial recognition purposes, please allow us access to your camera.' \
                '\n       Two pictures are required. Please press key a to take them.'
        canvas.create_text(width / 16, 8.2 * height / 16, anchor=NW, text=third, font=(font, 18))
        accept_button = Button(root, text='Accept', command=lambda: validation_window(accept_button), font=(font, 15),
                               background="white")
        canvas.create_window(7 * width / 64, 10.3 * height / 16, anchor=NW, window=accept_button)
    else:
        count_fail_id += 1
        messagebox.showerror("Error", text)
        if count_fail_id > 3:
            field.config(state='disabled')
            accept_butt.config(state='disabled')


def validation_window(accept_button):
    global count_fail_cap
    print(count_fail_cap)
    take_pic_of_user(dir_cam)
    images_id_list = face_detected(dir_id)
    images_cam_list = face_detected(dir_cam)
    comparation_list = []
    comparation_pics = 0
    try:
        _, comparation_pics = comparation(Image.open(images_cam_list[0]), Image.open(images_cam_list[1]))
    except:
        validation_window(accept_button)
    if count_fail_cap >= 2:
        accept_button.config(state='disabled')
        messagebox.showinfo(
            message='You have reached the number of attempts. Please contact your entity for further information.',
            title='Warning!')
        canvas.quit()
    else:
        for image in images_cam_list:
            user_pic = Image.open(image)
            user_id = Image.open(images_id_list[0])
            try:
                comparation_list.append(comparation(user_pic, user_id)[0])
            except:
                validation_window(accept_button)
        if not all(comparation_list) or comparation_pics == 0:
            count_fail_cap += 1
            text = 'Pictures do not match. Please try again.'
            messagebox.showerror("Error", text)
            validation_window(accept_button)
        else:
            text = 'Successful face recognition'
            accept_button.config(state='disabled')
            canvas.create_text(17 * width / 64, 10.5 * height / 16, anchor=NW, text=text,
                               font=(font, 18), fill="green")
            validation_text = 'Now that we have validated your identity, please continue to the following' \
                              '\nwebsite to complete your request.'
            canvas.create_text(width / 16, 12 * height / 16, anchor=NW, text=validation_text,
                               font=(font, 20), fill=colorrect)
            next_button = Button(root, text='Next', command=lambda: next_step(),
                                 font=(font, 15),
                                 background="white")
            canvas.create_window(15 * width / 16, 14.5 * height / 16, anchor=N, window=next_button)


def next_step():
    canvas.quit()


window()
root.mainloop()
