import sqlite3
from sqlite3 import Error
from conexao_banco import variavel_conexao
import os

os.system('cls')
print("\nALTERAR REGISTRO\n")
id_reg = int(input("Digite o ID do registro que deseja alterar: "))
novo_nome = input("Digite o novo nome do registro: ")
novo_sobrenome = input("Digite o novo sobrenome do registro: ")
nova_idade = int(input("Digite a nova idade do registro: "))
novo_sexo = input("Digite o novo sexo do registro: ")

atualizar_registros = f"""
UPDATE tb_formulario 
SET T_Nome = '{novo_nome}', T_Sobrenome  = '{novo_sobrenome}', N_Idade = '{nova_idade}', T_Sexo = '{novo_sexo}'
WHERE N_ID = '{id_reg}'
"""

def atualizarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally: 
        print("\nRegistro alterado/atualizado!\n")
        os.system('pause'),os.system('cls')

atualizarRegistro(variavel_conexao, atualizar_registros)
