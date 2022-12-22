import sqlite3
from sqlite3 import Error
from conexao_banco import variavel_conexao
import os

os.system('cls')
print("\nCRIAR TABELA\n")
def criarTabela(conexao, sql):
    global nova_tabela
    nova_tabela = """
    CREATE TABLE tb_formulario(
    N_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    T_Nome varchar(30) NOT NULL,
    T_Sobrenome varchar(30) NOT NULL,
    N_Idade integer(3) NOT NULL,
    T_Sexo varchar (20)
)
"""
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        print("\nTabela criada!\n")
        os.system('pause'),os.system('cls')
    except Error as excecao:
        print(excecao)
    
criarTabela(variavel_conexao, nova_tabela)

variavel_conexao.close()