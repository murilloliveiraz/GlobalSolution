#Objetivo: arquivo responsável pelos endpoints

from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from controller import viagensController

#com o __name__ ele assume o nome do módulo principal
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = True
CORS(app, origins='*')

#Rota padrão
@app.route('/', methods=['GET'])
def hello():
    return make_response(
        jsonify({"message": "Olá! Bem vindo ao backend da SustainTravel. Documentação em <https://github.com/murilloliveiraz/GlobalSolution>" })
    )
    
#Rota que retorna todas as viagens cadastradas no banco de dados
@app.route('/viagens', methods=['GET'])
def getViagens():
    return make_response(
        viagensController.getAllViagens()
    )

app.run()