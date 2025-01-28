#arquivo para montagem de logica de funcionamento do programa
#endpoints
#banco de dados
#inicialição do app
from flask import Flask, jsonify
from flask_restful import Api
from resources import Postagem
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'banco.db')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}' #criando o banco de dados na pasta raiz.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #desativa o rastreamento de modificações para o banco de dados
api = Api(app)


# a partir daqui colocar os endpoints para os metodos do resource

api.add_resource(Postagem, '/postagens')


#__________________________________________________________________________

if __name__ == '__main__':
    from sqlalchemy import banco #importando o banco aqui para so iniciar o processo de criação quando o app for chamado
    banco.init_app(app)
    with app.app_context():
        banco.create_all() #somente no contexto do app inicia o banco de dados

    app.run(debug=True)