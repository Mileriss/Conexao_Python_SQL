from formulario import *

#importando o módulo para utilizar o Banco de Dados SQL
import sqlite3
from sqlite3 import Error

print("Formulario para manipular banco de dados\n\n")

#Função para conectar ao banco de dados 'formulario'
def conexaoBanco():
    caminho = "C:\\Users\\s5057981\\OneDrive\\Documentos\\SQLite\\formulario.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as excecao:
        print(excecao)
    return conexao

var_conexao = conexaoBanco()


#Função para criar uma nova tabela
cols_tb = f"""
CREATE TABLE {nome_tb}(
    ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    {col1} VARCHAR(50) NOT NULL,
    {col2} VARCHAR(50) NOT NULL,
    {col3} INTEGER(5) NOT NULL,
    {col4} INTEGER(20) NOT NULL,
    {col5} VARCHAR(30) NOT NULL,
)
"""
def criarTB(conexao,query_sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(query_sql)
    except Error as excecao:
        print(excecao)

criarTB(var_conexao, cols_tb)

var_conexao.close()