from flask_restful import Resource
from Models.postagem import PostagemModel
from flask import request, jsonify
import datetime

class Postagem(Resource):
    def get(self, id_postagem):
        postagem = PostagemModel.find_by_id(id_postagem)
        if postagem:
            return jsonify(postagem.json())
        return {'message' : 'postagem não encontrada'}, 404

        else:
        

