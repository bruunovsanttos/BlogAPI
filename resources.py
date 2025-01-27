#aqui fica os metodos para atingir os endpoints da postagem
#metodos get, put, post e delete
from flask_restful import Resource, reqparse
from models import PostagemModel
import sqlite3

