#modleo de como deve ser a ideia do que se necessita para postagem
#modelo de criação do banco de dados com quantidade de caracteres e primary key
#criação tambem da def para tranformar em dict as infos

from sqlalchemy import banco, func
from datetime import datetime

class PostagemModel(banco.Model):
    __tablename__ = 'postagem'


    id_postagem = banco.Column(banco.String, primary_key=True)
    title = banco.Column(banco.String(50))
    content = banco.Column(banco.String(1000))
    category = banco.Column(banco.String(100))
    tags = banco.Column(banco.String(100))
    createdAt = banco.Column(banco.Datetime, default=func.now())
    updateAt = banco.Colum(banco.Datetime, default=func.now(), onupdate=func.now()) #onupdate=func.now() faz com que o valor dessa coluna seja automaticamente atualizado para a data/hora atual sempre que o registro for modificado.



#necessario ter id, titulo, conteudo, categoria, tags (mas pode deixar null), criado em , atualizado em.
    def __init__(self, id_postagem, title, content, category, tags, createdAt, updateAt):
        self.id_postagem = id_postagem
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
        self.createdAt = createdAt
        self.updateAt = updateAt


    def json(self):
        return {
            'id_postagem':self.id_postagem,
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'tags': self.tags,
            'createdAt': self.createdAt,
            'updateAt': self.updateAt
        }

    

    