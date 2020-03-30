'''
Created on 29 de mar de 2020

@author: lukit
'''


from Testes import Connection

my_database, db_connection = Connection.conexao() 


def inserir():
    nome = input("Digite o nome: ")
    fornecedor = input("Digite o fornecedor:")
    sql_statement = "INSERT INTO equipamento (nome,fornecedor) values(%s,%s)"
    values = (nome,fornecedor)
    my_database.execute(sql_statement,values)
    db_connection.commit()
    
def selecionar():
    sql_statement = "SELECT * FROM equipamento"
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    for x in output:
        print(x)
        
def selecionarChave():
    id = input("Digite o id que sera selecionado: ")
    sql_statement = "SELECT * FROM equipamento where id = {}".format(id)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    for x in output:
        print(x)
        
def update():
    id = input("Digite o ID do equipamento que sera alterado")
    nome = input("Digite o novo nome: ")
    fornecedor = input("Digite o novo fornecedor:")
    sql_statement = "UPDATE equipamento SET nome='{}',fornecedor = '{}' where id='{}'".format(nome,fornecedor,id)
    my_database.execute(sql_statement)
    db_connection.commit()
    
def excluir():
    id = input("Digite o id que sera excluido: ")
    sql_query = "DELETE FROM equipamento where id='{}'".format(id)
    my_database.execute(sql_query)
    db_connection.commit()
    
    
