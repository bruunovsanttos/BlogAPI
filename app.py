from flask import Flask, jsonify
from flask_restful import Api
from Resources.postagem import Postagem
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Postagem, '/postagem')

if __name__ == '__main__':
    app.run(debug=True)




