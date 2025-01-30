#aqui fica os metodos para atingir os endpoints da postagem
#metodos get, put, post e delete
from flask_restful import Resource, reqparse
from models import PostagemModel
import sqlite3

class Postagem(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('title', type=str, required=True, help="O campo 'title' não pode ser deixado em branco")
    argumentos.add_argument('content', type=str, required=True, help="o campo 'content' não pode ser deixado em branco")
    argumentos.add_argument('category', type=str)
    argumentos.add_argument('tags', type=str)



    def get(self, id_postagem):#procura postagem por ID
        #de alguma forma eu tenho que receber as informações do banco de dados
        #Tenho que fazer uma função no models para receber as postagens do banco
        postagem = PostagemModel.achar_postagem(id_postagem)
        if postagem:
            return postagem.json(), 200
        return{'message': 'Postagem not found.'}, 404 #erro por não achar nenhuma postagem


    def post(self, id_postagem):
        if PostagemModel.achar_postagem(id_postagem):
            return{'message': f"Postagem id '{id_postagem}' alredy exists"}, 400 #dando erro

        dados = Postagem.argumentos.parse_args()
        postagem = PostagemModel(id_postagem, **dados)
        try:
            postagem.save_post()
            return postagem.json(), 200

        except:
            return {'message': 'An internal erros ocurred trying save post'}, 500
        return postagem.json()

    def put(self, id_postagem):
        dados = Postagem.argumentos.parse_args()

        postagem_encontrada = PostagemModel.achar_postagem(id_postagem)

        if postagem_encontrada:
            postagem_encontrada.update_post(**dados)
            postagem_encontrada.save_post()
            return postagem_encontrada.json(), 200
        postagem = PostagemModel(id_postagem, **dados)
        try:
            postagem.save_post(), 200
        except:
            {'message': 'an internal error ocorred trying save post'}, 500

        return postagem.json(), 201 #created


    def delete(self, id_postagem):
        postagem = Postagem.argumentos.parse_args(id_postagem)

        if postagem:
            try:
                postagem.delete_post()
                return {'message': 'Post delete sucesfull'}, 200
            except:
                return {'message': 'An internal error occorred trying to delete post'}, 500
        return {'message': 'Postagem not found'}, 404





