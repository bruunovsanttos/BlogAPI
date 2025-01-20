from sqlalchemy import banco
from datetime import datetime




class PostagemModel(banco.Model):
    __tablename__ = 'postagem'  # estancia a tabela

    # estancia as colunas dessa tabela abaixo
    id_postagem = banco.Column(banco.String, primary_key=True)
    title = banco.Column(banco.String(80))  # estancia o nome com 80 caracteres
    content = banco.Column(banco.String(500))  # estancia estrelas com uma casa depois da virgula
    category = banco.Column(banco.String(150))  # estancia diaria com duas casa depois da virgula
    tags = banco.Column(banco.String(100))  # estancia com 40 caracteres o nome da cidade
    createdAt = banco.Column(banco.String(40))
    updateAt = banco.Column(banco.String(40))




    def __init__(self, id_postagem, title, content, category, tags, createdAt, updateAt):
        self.id_postagem = id_postagem
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
        self.createdAt = createdAt
        self.updateAt = updateAt

    def json(self):
        return{
            'id_postagem':self.id_postagem,
            'title' : self.title,
            'content' : self.content,
            'category' : self.category,
            'tags' : self.tags,
            'createdAt' : self.createdAt,
            'updateAt' : self.updateAt
        }
    @classmethod
    def postagem(cls, id_postagem):
        pass
