from database import connection
cursor = connection.db_sustaintravel.cursor()

def getAllTravels():
    cursor.execute(
        '''select * from tbl_viagem'''
    )
    
    result = cursor.fetchall()
    
    return result
