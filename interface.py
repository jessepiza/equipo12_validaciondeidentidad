from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.filedialog import askopenfile
import time


width = 1024
height = 1024
root = Frame(height=height, width = width,background="white")
root.pack(padx = 0,pady = 0)



def Grafica():
    context = "Para validar su identidad siga los siguientes pasos:"
    etiqueta = Label(text=context, font=("Verdana",20),background="white").place(x=45, y=45)
    first = """1.   Confirme el número de su identificación.
    Recuerde no usar puntos ni espacios."""
    etiqueta_1 = Label(text=first, font=("Verdana",18),background="white").place(x=45, y=150)
    id = "Ingrese su número de cédula aquí: "
    etiqueta_id = Label(text=id, font= ("Verdana",15),background="white").place(x=85, y=250)
    campo = Entry(root)
    campo.insert(0, "")
    campo.place(x=85, y=300)
    button = Button(root, text="Aceptar", command = lambda: cedula(campo.get()), font= ("Verdana",15),background="white").place(x=250,y=300)

def limpiar():
    root.destroy()


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg', '*jpg')])
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(text='File Uploaded Successfully!', font=("Verdana",18),foreground='green').place(x=55, y = 500)


def cedula(entry):
    id = int(entry)
    print(id)
    secd = """2.   Ingrese una foto de su cédula en donde se vea claro
    su foto y el número de identificación."""
    etiqueta_1 = Label(text=secd, font=("Verdana",18),background="white").place(x=45, y=400)
        # warn= "Ingrese el número de su cédula"
        # label = Label(text=warn, font= ("Verdana",12),background="white").place(x=350, y=300)
    lab = Label(text='Suba el documento', font=("Verdana",18),background="white").place(x= 45, y=550)
    button3 = Button(root, text ='Choose File', command = lambda:open_file(), font= ("Verdana",15),background="white").place(x=80,y=600)
    upld = Button(root, text='Upload Files', command = lambda:uploadFiles(), font= ("Verdana",15),background="white").place(x=80,y=650)

Grafica()
root.mainloop()
