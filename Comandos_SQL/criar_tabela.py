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

nova_tabela = """
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
        conectar = conexao.cursor()
        conectar.execute(sql)
        print("Tabela criada!")
    except Error as excecao:
        print(excecao)
    
criarTabela(variavel_conexao, nova_tabela)

variavel_conexao.close()