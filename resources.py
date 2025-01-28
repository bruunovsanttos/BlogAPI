#aqui fica os metodos para atingir os endpoints da postagem
#metodos get, put, post e delete
from flask_restful import Resource, reqparse
from models import PostagemModel
import sqlite3

class Postagem(Resource):
    def get(self):
        #de alguma forma eu tenho que receber as informações do banco de dados
        #Tenho que fazer uma função no models para receber as postagens do banco
        pass

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass



