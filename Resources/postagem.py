from flask_restful import Resource
from Models.postagem import PostagemModel
from flask import request, jsonify
import datetime

class Postagem(Resource):
    def get(self, id_postagem):
        postagem = PostagemModel.find_by_id(id_postagem)
        if postagem:
            return jsonify(postagem.json())
        return {'message': 'Postagem não encontrada'}, 404

    def put(self, id_postagem):
        pass

    def post(self):
        def post(self):
            # Recebe os dados da requisição
            dados = request.get_json()

            # Validação de campos obrigatórios
            if not dados or not dados.get('title') or not dados.get('content') or not dados.get('category'):
                return {'message': 'Campos title, content e category são obrigatórios.'}, 400

            try:
                # Cria uma nova postagem
                postagem = PostagemModel(
                    id_postagem= dados['id_postagem'],
                    title=dados['title'],
                    content=dados['content'],
                    category=dados['category'],
                    tags=dados.get('tags', []),
                    createdAt=datetime.datetime.utcnow(),
                    updateAt=datetime.datetime.utcnow()
                )

                # Adiciona e comita a postagem no banco
                Models.postagem(dados)

                return jsonify(postagem.json()), 201  # Retorna o objeto criado com status 201
            except Exception as e:
                return {'message': 'Erro ao criar postagem: ' + str(e)}, 500

    def delete(self, id_postagem):
        postagem = PostagemModel.find_by_id(id_postagem)

        if not postagem:
            return {'message':'Postagem não encontrada'}, 404

        else:
            try:
                postagem.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete postagem.'}, 500
            return {'message': 'Postagem delete'}
        


