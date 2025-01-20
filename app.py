from flask import Flask, jsonify
from flask_restful import Api
from Resources.postagem import Postagem


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Postagem, '/postagem')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    with app.app_context():
        banco.create_all()
    app.run(debug=True)




