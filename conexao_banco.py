#Importando o banco de dados SQLITE3
import sqlite3

#Importando as exceções em caso de erro
from sqlite3 import Error


def conexaoBanco():
    caminho = "C:\\Users\\s5057981\\OneDrive\\Documentos\\SQLite\\teste.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
        return conexao

var_conexao = conexaoBanco()
