# Objetivo: arquivo responsável pela manipulação de dados das viagens no banco de dados

#Importa a conexão com o banco de dados
from database import connection
cursor = connection.db_sustaintravel.cursor()

#Retorna todas as viagens da tabela de viagens no banco de dados
def getAllTravels():
    cursor.execute(
        '''select * from tbl_viagem'''
    )
    
    result = cursor.fetchall()
    
    return result
