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

#Inserindo registros manualmente
variavel_inserir_registros = "INSERT INTO tb_teste (T_Nome, T_Sobrenome, N_Idade, T_Sexo) VALUES ('Rafael','Mileris', 25, 'Masculino')"

def inserirRegistro(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally:
        print("Registro inserido!")

inserirRegistro(variavel_conexao, variavel_inserir_registros)


#Inserindo registros com inputs do usuário
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
print("\nDigite seu sexo (Masculino ou Feminino")
sexo = input("Digite aqui: ")

variavel_inserir_input = "INSERT INTO tb_teste (T_Nome, T_Sobrenome, N_Idade, T_Sexo) VALUES ('"+nome+"', '"+sobrenome+"', '"+idade+"', '"+sexo+"')"

def inserirInput(conexao, sql):
    try:
        conectar = conexao.cursor()
        conectar.execute(sql)
        variavel_conexao.commit()
    except Error as excecao:
        print(excecao)
    finally:
        print("Registro inserido!")

inserirInput(variavel_conexao, variavel_inserir_input)

