import sqlite3
from sqlite3 import Error
from conexao_banco import variavel_conexao
import os

os.system('cls')
print("\nCONSULTAR REGISTROS\n")
def visualizarRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        resultado = conectar.fetchall()
    except Error as excecao:
        print(excecao)
    return resultado
    
consultar_registros = "SELECT * FROM tb_formulario"
resultado = visualizarRegistro(variavel_conexao, consultar_registros)

for registro in resultado:
    print(f"- {registro}")

print("\n\n")
os.system('pause'),os.system('cls')

