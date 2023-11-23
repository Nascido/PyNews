from tkinter import *


class PyNews:
    def __init__(self, usuarios):
        self.users = usuarios

    def login(self):
        def checklogin():
            usrname = username_entry.get()
            password = password_entry.get()
            encontrado = False

            for usr in self.users:
                name = usr.getusr()
                if usrname == name:
                    senha = usr.getsenha()
                    encontrado = True
                    if senha == password:
                        print("Usuário Autenticado")

                    else:
                        print("Senha incorreta")

            if not encontrado:
                print("Usuário Inexistente")

        # Login window
        login = Tk()
        login.title("Login de Usuário")
        login.geometry("350x400")

        # widgets
        login_label = Label(login, text="Login")
        username_label = Label(login, text="Usuário")
        username_entry = Entry(login)
        password_label = Label(login, text="Senha")
        password_entry = Entry(login, show='*')
        login_button = Button(login, text='Entrar', command=checklogin)

        # Placing widgets
        login_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2)

        login.mainloop()
