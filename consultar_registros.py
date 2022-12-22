import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = "C:\\Users\\s5057981\\OneDrive\\Documentos\\SQLite\\teste.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as excecao:
        print(excecao)
    return conexao

variavel_conexao = conexaoBanco()


def visualizarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        resultado = conectar.fetchall()
    except Error as excecao:
        print(excecao)
    return resultado
    
consultar_registros = "SELECT * FROM tb_teste"
resultado = visualizarRegistro(variavel_conexao, consultar_registros)

for registro in resultado:
    print(f"- {registro}")

