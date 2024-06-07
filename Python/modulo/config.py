#Objetivo: arquivo com mensagens padrão para o retorno dos endpoints

#ERRO
ERROR_NOT_FOUND = {"status": 404, "message": 'Nenhum registro foi encontrado.'}
ERROR_REQUIRED_FIELD = {"status": 401, "message": 'Campos obrigatórios não preenchidos'}

#SUCCESS
SUCCESS_REQUEST = {"status": 200, "message": 'Requisição bem sucedida.'}