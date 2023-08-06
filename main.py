from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title('Авторизация')
root.geometry('450x230')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def enter():
    user_name_entry = username_entry.get()
    user_password_entry = password_entry.get()
    if len(user_password_entry) > 0:
        messagebox.showinfo('Авторизация прошла!', f'Добро пожаловать {user_name_entry}')
    else:
        messagebox.showinfo('Авторизация не прошла!!!', 'Заполните оба поля!')


creat_tabl = """CREATE TABLE IF NOT EXISTS base(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            password TEXT
            )"""

def click():
    username = username_entry.get()
    password = password_entry.get()
    if len(username)>0 and len(password)>0:
        with sqlite3.connect("data_base.db") as sql_coonnect:
                    cursors = sql_coonnect.cursor()
                    cursors.execute(creat_tabl)
                    cursors.execute(""" INSERT INTO base VALUES(NULL,?,?)""",(username,password))
        messagebox.showinfo('Авторизация прошла!', f' Вы вошли в систему {username}')
    else:
        messagebox.showinfo('Ошибка!', 'Заполните оба поля!')

    username_entry.delete(0, END)
    password_entry.delete(0, END)

main_label = Label(root, text='Авторизация', font='Arial 15 bold', bg='black', fg='white')
main_label.pack()

username_label = Label(root, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white')
username_label.pack()

username_entry = Entry(root, bg='black', fg='lime', font='Arial 12', justify='right')
username_entry.pack()

user_password = Label(root,  text='Введите пароль', font='Arial 11 bold', bg='black', fg='white')
user_password.pack()

password_entry = Entry(root, bg='black', fg='lime', font='Arial 12', justify='right')
password_entry.pack()

btn1 = Button(root, text='Зарегестрироваться', command=click, bg='red', font='Arial 10 bold')
btn1.pack(padx=5, pady=5)

btn2 = Button(root, text='Войти', command=enter, bg='blue', font='Arial 10 bold')
btn2.pack()


root.mainloop()


