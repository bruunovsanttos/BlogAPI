#modleo de como deve ser a ideia do que se necessita para postagem
#modelo de criação do banco de dados com quantidade de caracteres e primary key
#criação tambem da def para tranformar em dict as infos

from sqlalchemy import banco

class PostagemModel(banco.Model):
    pass

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
        pass

    