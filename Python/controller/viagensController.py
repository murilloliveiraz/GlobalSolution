from model import viagensDAO, tagsDAO
from flask import jsonify
from modulo import config
import functools

def getAllViagens():
    viagens = viagensDAO.getAllTravels()
    
    if not viagens:
        return jsonify(config.ERROR_NOT_FOUND), config.ERROR_NOT_FOUND["status"]
    else:
        viagensFormatted = list()
        
        for viagem in viagens:
            viagensFormatted.append({
                'id': viagem[0],
                'nome': viagem[1],
                'qtd_dias': viagem[2],
                'qtd_noites': viagem[3],
                'avaliacao_media': viagem[4],
                'imagem': viagem[5],
                'tags': tagsDAO.getTagsByIdViagem(viagem[0])
            })
        
        return jsonify({
            "status": config.SUCCESS_REQUEST["status"],
            "message": config.SUCCESS_REQUEST["message"],
            "data": viagensFormatted
        }), config.SUCCESS_REQUEST["status"]
