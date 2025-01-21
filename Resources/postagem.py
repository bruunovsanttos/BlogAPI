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
        pass

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
        


