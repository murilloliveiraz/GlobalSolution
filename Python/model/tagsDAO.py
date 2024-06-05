from database import connection
cursor = connection.db_sustaintravel.cursor()

def getTagsByIdViagem(idViagem):
    cursor.execute(
        f'''select tbl_tag.nome from tbl_tag_viagem
                inner join tbl_tag
                    on tbl_tag.id = tbl_tag_viagem.id_tag
                where tbl_tag_viagem.id_viagem = {idViagem}'''
    )
    
    result = cursor.fetchall()
    
    return result
