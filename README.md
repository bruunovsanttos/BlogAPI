# BlogAPI
Desenvolvimento de API para blog do [Roadmap.sh](https://roadmap.sh/projects/blogging-platform-api)  
Esta é uma API RESTful para uma plataforma de blog pessoal. Ela permite que os usuários criem, leiam, atualizem, excluam e filtrem postagens de blog. A API segue os princípios do padrão REST e utiliza os métodos HTTP adequados para cada operação  


### Metas
Os objetivos deste projeto são:

* Entender o que são as APIs RESTful, incluindo melhores práticas e convenções  
* Criar uma API RESTful  
* Métodos HTTP comuns como GET, POST, PUT, DELETE  
* Códigos de status e tratamento de erros em APIs  
* Executar operações CRUD usando uma API  
* Trabalhar com bancos de dados  

### Requisitos
Você deve criar uma API RESTful para uma plataforma de blog pessoal. A API deve permitir que os usuários realizem as seguintes operações:  


Criar uma nova postagem de blog  
Atualizar uma postagem de blog existente  
Excluir uma postagem de blog existente  
Obtenha uma única postagem de blog  
Obter todas as postagens do blog  
Filtrar postagens de blog por um termo de pesquisa  

## Tecnologias Utilizadas

|Tecnologia	|Descrição|
|---|----|
|Python	|Linguagem de programação para desenvolver a API|
|Flask|	Framework web para desenvolvimento de APIs|  
|Flask-RESTful	|Extensão do Flask para facilitar a criação de APIs RESTful  |
|SQLAlchemy	|ORM (Object Relational Mapper) para interagir com bancos de dados relacionais|
|SQLite	|Banco de dados relacional utilizado para armazenamento de dados|
|reqparse	|Biblioteca para análise e validação de parâmetros em requisições HTTP|

  

## Estrutura do projeto

blog-api/  
│  
├── app.py  
├── init  
├── banco.db  
├── extensions   
├── models.py   
├── resources.py   
├── LICENSE  
└── README.md  


* __App.py__: Arquivo principal onde a aplicação Flask é configurada
* __init__: inicializador do programa
* __banco.db__: Banco de dados SQLite gerado automaticamente com SQLAlchemy
* __Extensions__: Pasta para extensões do Flask (utilizada como a configuração do banco de dados)
* __models.py__: Definição do modelo de Postagem
* __resources.py__: Definição dos recursos (Postagem e PostagensLista)  
* __License__: Licença MIT do repositório
* __README.md__: Documentação do projeto


