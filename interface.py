from tkinter import *
from tkinter import messagebox as mg
from newsapi import NewsApiClient


class Interface:
    def __init__(self, usuarios):
        self.users = usuarios
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
                        self.acess()

                    else:
                        print("Senha incorreta")
                        mg.showinfo("Falha no Login", "Senha Incorreta!", icon='error')

            if not encontrado:
                print("Usuário Inexistente")
                mg.showinfo("Falha no Login", "Usuário não encontrado!", icon='error')

        # Login window
        login = Tk()
        login.title("Login de Usuário")
        login.geometry("350x200")

        frame_login = Frame(login)
        frame_login.pack()

        # widgets
        login_label = Label(frame_login, text="Login")
        username_label = Label(frame_login, text="Usuário")
        username_entry = Entry(frame_login)
        password_label = Label(frame_login, text="Senha")
        password_entry = Entry(frame_login, show='*')
        login_button = Button(frame_login, text='Entrar', command=checklogin)

        # Placing widgets
        login_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2)

        login.mainloop()

    def acess(self):
        nome = self._usr.getname()
        intro_usario = f"Bem vindo {nome}"

        sistem = Tk()
        welcome = Label(sistem, text=intro_usario)
        welcome.pack()

        sistem.mainloop()


class PyNews(Interface):
    def __init__(self, usuarios):
        super().__init__(usuarios)
        self.key = "d4bb5b7f812541389fa49cabc50659d0"
        self.api = NewsApiClient(api_key=self.key)
        self.q = 'manchete'

    def acess(self):
        self.news()

    def news(self):
        nome = self._usr.getname()
        intro_usario = f"Bem vindo {nome}"

        def getnews():
            busca = search_entry.get()
            from_colected = from_date_entry.get()
            to_colected = to_date_entry.get()
            old_date = False

            # Oldest news 2023-10-23
            if from_colected != '':
                from_dia, from_mes = from_colected.strip().split('/')
                if len(from_dia) == 1:
                    from_dia = '0' + from_dia

                from_data = f"2023-{from_mes}-{from_dia}"

                if int(from_mes) < 10:
                    old_date = True
                elif int(from_dia) < 23:
                    old_date = True

            else:
                from_data = None

            if to_colected != '':
                to_dia, to_mes = to_colected.strip().split('/')
                if len(to_dia) == 1:
                    to_dia = '0' + to_dia

                to_data = f"2023-{to_mes}-{to_dia}"
            else:
                to_data = None

            if busca != '':
                self.q = busca

            if old_date:
                mg.showinfo("Data Inválida", "Notícia mais antiga: 23/10")

            # Headlines
            news = self.api.get_everything(q=self.q, language='pt', from_param=from_data, to=to_data)

            # Clear
            text.delete(1.0, END)

            # Display
            for article in news['articles']:
                title = article['title']
                article_date = article['publishedAt']
                article_date = article_date[0:10]

                article_ano, article_mes, article_dia = article_date.split('-')

                article_date = f"{article_dia}/{article_mes}/{article_ano}"

                if title is not None:
                    if title[0] != '[':
                        text.insert(END, f"{title} ({article_date})\n\n")

        # News Window
        win = Tk()
        win.title('News App')
        news_frame = Frame(win)
        search_frame = Frame(win)
        date_frame = Frame(win)

        # Frames
        news_frame.grid(row=0, column=0, columnspan=2)
        search_frame.grid(row=1, column=1)
        date_frame.grid(row=1, column=0)

        # Intro
        intro = Label(news_frame, text=intro_usario)

        # News Text
        text = Text(news_frame, height=20, width=125)

        # Search Context
        search_label = Label(search_frame, text="Assunto")
        search_entry = Entry(search_frame)

        # From Date
        from_date_label = Label(date_frame, text="Inicio (dia/mes)")
        from_date_entry = Entry(date_frame)

        # To Date
        to_date_label = Label(date_frame, text="Fim (dia/mes)")
        to_date_entry = Entry(date_frame)

        # Buttons
        enter = Button(search_frame, text="Procurar", command=getnews)

        # Layout
        intro.grid(row=0, column=0)
        text.grid(row=1, column=0)

        from_date_label.grid(row=0, column=0)
        from_date_entry.grid(row=0, column=1)

        to_date_label.grid(row=1, column=0)
        to_date_entry.grid(row=1, column=1)

        search_label.grid(row=0, column=0)
        search_entry.grid(row=0, column=1)
        enter.grid(row=1, column=0, columnspan=2)

        win.mainloop()
