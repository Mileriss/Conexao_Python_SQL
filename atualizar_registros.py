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


atualizar_registros = """
UPDATE tb_teste 
SET T_Nome = 'Antonia', T_Sobrenome  = 'Joyce', N_Idade = 23, T_Sexo = 'Feminino'
WHERE N_ID = 2
"""

atualizar_registros_2 = """
UPDATE tb_teste
SET T_Nome = 'Maria', T_Sobrenome = 'Aparecida', N_Idade = 50, T_Sexo = 'Feminino'
WHERE N_ID = 3
"""

def atualizarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally: 
        print("Registro alterado/atualizado!")

atualizarRegistro(variavel_conexao, atualizar_registros)
