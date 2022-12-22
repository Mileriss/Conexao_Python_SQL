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


deletar_registros = "DELETE FROM tb_teste WHERE N_ID = 1"

def deletarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally:
        print("Registro deletado!")
    
deletarRegistro(variavel_conexao, deletar_registros)

