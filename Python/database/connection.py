import os
from dotenv import load_dotenv
import mysql.connector

#Carrega as informações de acesso do banco de dados do arquivo .env
load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}

#Conecta com o banco passando as informações de acesso
db_sustaintravel = mysql.connector.connect(**db_config)

#Verifica se foi conectado corretamente
if db_sustaintravel.is_connected():
    print('Conectado ao banco de dados MySQL')
  
else:
    print('ERRO: Não foi possível conectar ao banco de dados MySQL')