import datetime


class PostagemModel():

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
