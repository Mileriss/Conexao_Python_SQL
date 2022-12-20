import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = f"\\Users\\s5057981\\OneDrive\\Documentos\\SQLite\\teste.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as excecao:
        print(excecao)
    return conexao

var_conexao = conexaoBanco()

nv_tb = """
CREATE TABLE tb_teste(
    N_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    T_Nome varchar(30) NOT NULL,
    T_Sobrenome varchar(30) NOT NULL,
    N_Idade integer(3) NOT NULL,
    T_Sexo varchar (20)
)
"""

def criarTabela(conexao, sql):
    try:
        con = conexao.cursor()
        con.execute(sql)
        print("Tabela criada!")
    except Error as excecao:
        print(excecao)
    
criarTabela(var_conexao, nv_tb)

var_conexao.close()