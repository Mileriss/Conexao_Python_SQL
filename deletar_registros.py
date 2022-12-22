import sqlite3
from sqlite3 import Error
from conexao_banco import variavel_conexao
import os

os.system('cls')
print("\nDELETAR REGISTRO\n")
sel_id = input("Digite o Nº de ID que deseja excluir: ")
deletar_registros = "DELETE FROM tb_formulario WHERE N_ID = '"+sel_id+"'"

def deletarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally:
        print("\nRegistro deletado!\n")
        os.system('pause'),os.system('cls')
    
deletarRegistro(variavel_conexao, deletar_registros)

