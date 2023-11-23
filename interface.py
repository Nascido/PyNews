from tkinter import *
from newsapi import NewsApiClient


class PyNews:
    def __init__(self, usuarios):
        self.users = usuarios
        self.key = "f0092823669c4b4d8e260b1eb30cfc4d"
        self.api = NewsApiClient(api_key=self.key)
        self._usr = None

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
                        self._usr = usr
                        self.news()

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

    def news(self):
        nome = self._usr.getname()
        intro_usario = f"Bem vindo {nome}"
        interesse = "Mundo"

        def getnews():
            # Top Headlines
            news = self.api.get_everything(q=interesse, language='pt')

            # Clear
            text.delete(1.0, END)

            # Display
            for article in news['articles']:
                text.insert(END, f"{article['title']} ({article['publishedAt']})\n\n")

        # News Window
        win = Tk()
        win.title('News App')

        # Intro
        intro = Label(win, text=intro_usario)

        # News Text
        text = Text(win, height=20, width=150)

        # Search Context
        search_label = Label(win, text="Assunto")
        search_entry = Entry(win)

        # From Date
        from_date_label = Label(win, text="Inicio (Mes e Dia)")
        from_mes_entry = Entry(win)
        from_dia_entry = Entry(win)

        # To Date
        to_date_label = Label(win, text="Fim (Mes e Dia)")
        to_mes_entry = Entry(win)
        to_dia_entry = Entry(win)

        # Buttons
        enter = Button(win, text="Procurar", command=getnews)

        win.mainloop()
