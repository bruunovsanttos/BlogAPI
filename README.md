# BlogAPI 🔍
Desenvolvimento de API para blog do [Roadmap.sh](https://roadmap.sh/projects/blogging-platform-api)  
Esta é uma API RESTful para uma plataforma de blog pessoal. Ela permite que os usuários criem, leiam, atualizem, excluam e filtrem postagens de blog. A API segue os princípios do padrão REST e utiliza os métodos HTTP adequados para cada operação  


### Metas 📝✅
Os objetivos deste projeto são:

* Entender o que são as APIs RESTful, incluindo melhores práticas e convenções  
* Criar uma API RESTful  
* Métodos HTTP comuns como GET, POST, PUT, DELETE  
* Códigos de status e tratamento de erros em APIs  
* Executar operações CRUD usando uma API  
* Trabalhar com bancos de dados  

### Requisitos 📋
Você deve criar uma API RESTful para uma plataforma de blog pessoal. A API deve permitir que os usuários realizem as seguintes operações:  


Criar uma nova postagem de blog  
Atualizar uma postagem de blog existente  
Excluir uma postagem de blog existente  
Obtenha uma única postagem de blog  
Obter todas as postagens do blog  
Filtrar postagens de blog por um termo de pesquisa  

## Tecnologias Utilizadas 💻

| Tecnologia	        |Descrição|
|--------------------|----|
| **Python**         |Linguagem de programação para desenvolver a API|
| **Flask**          |	Framework web para desenvolvimento de APIs|  
| **Flask-RESTful**	 |Extensão do Flask para facilitar a criação de APIs RESTful  |
| **SQLAlchemy**	    |ORM (Object Relational Mapper) para interagir com bancos de dados relacionais|
| **SQLite**	        |Banco de dados relacional utilizado para armazenamento de dados|

  

## Estrutura do Projeto  🧱
```
/
├── app.py            # Inicialização do app, configurações e endpoints
├── models.py         # Definição do modelo de dados da postagem
├── resources.py      # Implementação dos endpoints REST
├── extensions.py     # Extensões do Flask (Banco de dados)
├── banco.db          # Banco de dados SQLite gerado dinamicamente
└── requirements.txt  # Dependências do projeto
```

### `app.py`
Responsável por inicializar o Flask, configurar o banco de dados SQLite e definir os endpoints principais da API.

### `models.py`
Define a estrutura do banco de dados com SQLAlchemy, incluindo os campos `id_postagem`, `title`, `content`, `category`, `tags`, `createdAt` e `updateAt`.

### `resources.py`
Contém as classes que implementam os endpoints RESTful com os métodos `GET`, `POST`, `PUT` e `DELETE`.

### `extensions.py`
Arquivo para configuração do banco de dados e extensões utilizadas.


## Configuração e Execução  🧮

  
1. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Execute a API:**
   ```sh
   python app.py
   ```

A API será iniciada no `http://127.0.0.1:5000/`

## Endpoints  🔚
### **Criar Postagem**
- **Rota:** `POST /postagens/<id_postagem>`
- **Parâmetros:**
  ```json
  {
    "title": "Título da Postagem",
    "content": "Conteúdo da postagem",
    "category": "Categoria",
    "tags": "tag1, tag2"
  }
  ```
- **Resposta:**
  ```json
  {
    "id_postagem": "1",
    "title": "Título da Postagem",
    "content": "Conteúdo da postagem",
    "category": "Categoria",
    "tags": "tag1, tag2",
    "createdAt": "2025-01-31 15:53:17",
    "updateAt": "2025-01-31 15:53:17"
  }
  ```

### **Obter Todas as Postagens**
- **Rota:** `GET /postagens`
- **Resposta:**
  ```json
  {
    "Postagens": [
      {
        "id_postagem": "1",
        "title": "Título da Postagem",
        "content": "Conteúdo da postagem",
        "category": "Categoria",
        "tags": "tag1, tag2",
        "createdAt": "2025-01-31 15:53:17",
        "updateAt": "2025-01-31 15:53:17"
      }
    ]
  }
  ```

### **Obter Postagem Específica**
- **Rota:** `GET /postagens/<id_postagem>`
- **Resposta:**
  ```json
  {
    "id_postagem": "1",
    "title": "Título da Postagem",
    "content": "Conteúdo da postagem",
    "category": "Categoria",
    "tags": "tag1, tag2",
    "createdAt": "2025-01-31 15:53:17",
    "updateAt": "2025-01-31 15:53:17"
  }
  ```

### **Atualizar Postagem**
- **Rota:** `PUT /postagens/<id_postagem>`
- **Parâmetros:** Mesma estrutura do POST
- **Resposta:** Postagem atualizada

### **Deletar Postagem**
- **Rota:** `DELETE /postagens/<id_postagem>`
- **Resposta:**
  ```json
  { "message": "Post delete successful" }
  ```


## Melhorias Futuras  💡
- Implementação de autenticação e autorização.
- Paginação para a listagem de postagens.
- Testes unitários para garantir a confiabilidade do sistema.
- Melhorias na pesquisa de postagens por termos e tags.

## Autor
Desenvolvido por Bruno Vieira Santos.


