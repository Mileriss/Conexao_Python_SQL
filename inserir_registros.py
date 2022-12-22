import sqlite3
from sqlite3 import Error
from conexao_banco import variavel_conexao
import os

os.system('cls')
print("\nINSERIR NOVO REGISTRO\n")
#Inserindo registros com inputs do usuário
nome = input("Digite um nome: ")
sobrenome = input("Digite um sobrenome: ")
idade = int(input("Digite uma idade: "))
print("Digite seu sexo (Masculino ou Feminino")
sexo = input("Digite aqui: ")

variavel_inserir_input = f"INSERT INTO tb_formulario (T_Nome, T_Sobrenome, N_Idade, T_Sexo) VALUES ('{nome}', '{sobrenome}', '{idade}', '{sexo}')"

def inserirInput(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally:
        print("\nRegistro inserido!\n")
        os.system('pause'),os.system('cls')

inserirInput(variavel_conexao, variavel_inserir_input)

