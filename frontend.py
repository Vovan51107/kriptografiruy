from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import kripto
import pyperclip



def s_new():
    if txt.get() == '' or txt2.get() == '':
        messagebox.showinfo('Error 1', 'Ошибка! Поля ввода пустые!')  
    else:
        global texte
        texte = kripto.kriptografiruy(str(txt.get()), int(txt2.get()))
        lbl4.configure(text= texte)


def enters():
    if lbl4.cget('text') == '(вывод)':
        messagebox.showinfo('Error 2', 'Ошибка! Отсутствует преобразованный текст!')  
    else:
        pyperclip.copy(lbl4.cget('text'))
        pyperclip.paste()


if __name__ == '__main__':
    window = Tk()
    window.title("Encoder")
    window.geometry('800x500')
    lbl = Label(window, text="Введите текст", font=("Arial Bold", 25))  
    lbl.grid(column=0, row=0)
    txt = Entry(window, font=('Aerial', 25))  
    txt.grid(column=0, row=1)  
    lbl3 = Label(window, text="Смещение", font=("Arial Bold", 25))  
    lbl3.grid(column=0, row=2)
    txt2 = Entry(window, font=('Aerial', 20), width=5)  
    txt2.grid(column=0, row=3)
    lbl2 = Label(window, text="Вывод:", font=("Arial Bold", 25))  
    lbl2.grid(column=0, row=6)
    lbl4 = Label(window, text='(вывод)', font=("Arial", 20))  
    lbl4.grid(column=1, row=6)
    texte = ''

    btns = Button(window, text="Преобразовать", bg="green", fg="white", height=10, width=25, command=s_new) 
    btns.grid(column=3, row=2)

    btn2 = Button(window, text="Скопировать", bg="white", fg="orange", height=10, width=25, command=enters)
    btn2.grid(column=3, row=4)
    window.mainloop()