# definindo os campos do banco de dados
# os passos obrigatorios sao importar o mysql.connector, criar a conexao, criar o cursor, criar a tabela, inserir os dados, salvar as alteracoes e fechar a conexao

import mysql.connector

# criando a conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)

# criando o cursor objecto
cursor = conexao.cursor()

#criando o banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS crm_db")
# mensagem se estiver criado ou se ja existir
print("Banco de dados criado ou já existe.")

#criando a tabela