# Objetivo: arquivo responsável pela manipulação de dados das tags no banco de dados

#Importa a conexão com o banco de dados
from database import connection
cursor = connection.db_sustaintravel.cursor()

#Função para retornar tags pelo id de viagens
def getTagsByIdViagem(idViagem):
    cursor.execute(
        f'''select tbl_tag.nome from tbl_tag_viagem
                inner join tbl_tag
                    on tbl_tag.id = tbl_tag_viagem.id_tag
                where tbl_tag_viagem.id_viagem = {idViagem}'''
    )
    
    result = cursor.fetchall()
    
    return result
