from sqlalchemy import banco
from datetime import datetime




class PostagemModel(banco.Model):
    __tablename__ = 'postagem'  # estancia a tabela

    # estancia as colunas dessa tabela abaixo
    id_postagem = banco.Column(banco.String, primary_key=True)
    title = banco.Column(banco.String(80))
    content = banco.Column(banco.text)
    category = banco.Column(banco.String(150))
    tags = banco.Column(banco.String(100))
    createdAt = banco.Column(banco.DateTime, default=datetime.utcnow)
    updateAt = banco.Column(banco.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)




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
    def find_by_id(cls, id_postagem):
        return cls.query.filter_by(id_postagem=id_postagem).first()
    @classmethod
    def postagem(cls, id_postagem):
        pass
