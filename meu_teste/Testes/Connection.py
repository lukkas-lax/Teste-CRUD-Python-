'''
Created on 29 de mar de 2020

@author: lukit
'''

import mysql.connector 

def conexao():
    db_connection = mysql.connector.connect(host="localhost",user="root",passwd="Lax0310ri",database="testepy")
    my_database = db_connection.cursor()
    return my_database, db_connection
    





