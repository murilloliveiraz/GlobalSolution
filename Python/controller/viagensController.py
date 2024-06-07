#Objetivo: arquivo responsavel pelo tratamento de dados

from model import viagensDAO, tagsDAO
from flask import jsonify
from modulo import config

#Função que retorna todas as viagens
def getAllViagens():
    viagens = viagensDAO.getAllTravels()
    
    #Se não houver viagem retorna um erro padrão de not found com o http code 404
    if not viagens:
        return jsonify(config.ERROR_NOT_FOUND), config.ERROR_NOT_FOUND["status"]
    else:
        viagensFormatted = list()
        
        #Formata o retorno da função
        for viagem in viagens:
            viagensFormatted.append({
                'id': viagem[0],
                'nome': viagem[1],
                'qtd_dias': viagem[2],
                'qtd_noites': viagem[3],
                'avaliacao_media': viagem[4],
                'imagem': viagem[5],
                'preco': viagem[6],
                'tags': tagsDAO.getTagsByIdViagem(viagem[0])
            })
        
        #Retorna os dados, criando um JSON e retornando o http code 200
        return jsonify({
            "status": config.SUCCESS_REQUEST["status"],
            "message": config.SUCCESS_REQUEST["message"],
            "data": viagensFormatted
        }), config.SUCCESS_REQUEST["status"]
