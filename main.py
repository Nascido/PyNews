from user import User
from interface import PyNews

usuarios = []
with open('usuarios.txt', 'r') as file:
    for line in file:
        usuario, nome, senha = line.strip().split(' - ')
        usr = User(usuario, nome, senha)
        usuarios.append(usr)

gui = PyNews(usuarios)

gui.news()
