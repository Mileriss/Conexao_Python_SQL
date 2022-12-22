import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = "C:\\Users\\Rafael Mileris\\OneDrive\\SQLITE\\Bancos\\formulario.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as excecao:
        print(excecao)
    return conexao

variavel_conexao = conexaoBanco()