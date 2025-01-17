from flask import Flask, jsonify
from flask_restful import Api
from Resources.postagem import postagem

app = Flask(__name__)
api = Api(app)

api.add_resource(Postagem, '/postagem')

if __name__ == '__main__':
    app.run(debug=True)




