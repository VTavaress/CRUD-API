# CRUD-API
Gerenciamento de pessoas

Funcionalidades:
Criar uma nova pessoa com informações como apelido, nome, data de nascimento e stack.
Buscar uma pessoa por ID.
Buscar pessoas por termo, pesquisando no apelido e nome.
Atualizar os dados de uma pessoa existente.
Excluir uma pessoa do banco de dados.
Endpoints

1. Criar Pessoa
Método: POST
URL: /pessoas
Corpo da Requisição:

{
    "apelido": "string",
    "nome": "string",
    "nascimento": "YYYY-MM-DD",
    "stack": ["string"]
}

Resposta:
Código: 201 Created
Corpo:

{
    "message": "Pessoa criada com sucesso"
}

2. Buscar Pessoa por ID
Método: GET
URL: /pessoas/<int:pessoa_id>
Resposta:
Código: 200 OK
Corpo:

{
    "message": "Pessoa criada com sucesso"
}

3. Buscar Pessoas por Termo
Método: GET
URL: /pessoas?t=<termo>
Parâmetros de Consulta:
t (obrigatório): Termo para pesquisa.
Resposta:
Código: 200 OK
Corpo:

[
    {
        "id": 1,
        "apelido": "string",
        "nome": "string",
        "nascimento": "YYYY-MM-DD",
        "stack": ["string"]
    }
]

4. Atualizar Pessoa
Método: PUT
URL: /pessoas/<int:pessoa_id>
Corpo da Requisição:

{
    "apelido": "string",
    "nome": "string",
    "nascimento": "YYYY-MM-DD",
    "stack": ["string"]
}

Resposta:
Código: 200 OK
Corpo:

{
    "message": "Pessoa atualizada com sucesso"
}

5. Deletar Pessoa
Método: DELETE
URL: /pessoas/<int:pessoa_id>
Resposta:
Código: 200 OK
Corpo:

{
    "message": "Pessoa excluída com sucesso"
}

BIBLIOTECAS:
Flask
Propósito: É um microframework leve e flexível para construir aplicações web em Python.
Funcionalidades:
Roteamento: Mapeia URLs para funções específicas do seu código, permitindo criar diferentes páginas ou endpoints para sua aplicação.
Templates: Permite criar interfaces de usuário dinâmicas usando templates (como Jinja2), separando a lógica do seu código da apresentação visual.
Gerenciamento de requisições: Lidar com requisições HTTP (GET, POST, etc.) e gerar respostas adequadas.
Extensibilidade: Pode ser facilmente estendida com extensões para adicionar funcionalidades como autenticação, bancos de dados, etc.

request
Propósito: Um objeto do Flask que contém informações sobre a requisição HTTP que está sendo processada.
Funcionalidades:
Métodos HTTP: Acessar o método HTTP usado na requisição (GET, POST, PUT, DELETE, etc.).
Parâmetros: Obter os parâmetros da URL ou do corpo da requisição.
Cabeçalhos: Acessar os cabeçalhos da requisição, como o tipo de conteúdo ou o agente do usuário.
Cookies: Manipular cookies HTTP.

jsonify
Propósito: Uma função do Flask que converte dados Python em formato JSON (JavaScript Object Notation).
Funcionalidades:
Serialização: Transforma objetos Python (dicionários, listas) em strings JSON, que podem ser facilmente transmitidos e interpretados por JavaScript e outras linguagens.
Resposta HTTP: É comumente usada para retornar dados em formato JSON como resposta a uma requisição HTTP.

SQLAlchemy
Propósito: Um ORM (Object-Relational Mapper) poderoso para Python.
Funcionalidades:
Mapeamento objeto-relacional: Mapeia classes Python para tabelas em um banco de dados, permitindo que você interaja com o banco de dados usando objetos Python.
SQL: Permite escrever consultas SQL diretamente ou usar a linguagem de consulta declarativa do SQLAlchemy para construir consultas de forma mais Pythonica.
Transações: Gerencia transações de banco de dados para garantir a integridade dos dados.
Relacionamentos: Define relacionamentos entre objetos (um para um, um para muitos, muitos para muitos), como os que existem em um banco de dados relacional.

werkzeug.exceptions
Propósito: Um módulo que fornece exceções HTTP padrão para Flask.
Funcionalidades:
Exceções HTTP: Define exceções como BadRequest (requisição inválida) e NotFound (recurso não encontrado), que podem ser levantadas para indicar erros HTTP.
Gerenciamento de erros: Permite personalizar a forma como as exceções são tratadas e gerar respostas HTTP apropriadas.

datetime
Propósito: Um módulo padrão do Python para trabalhar com datas e horas.
Funcionalidades:
Objetos de data e hora: Cria e manipula objetos que representam datas e horas específicas.
Formatação: Permite formatar datas e horas de acordo com diferentes padrões.
Cálculos: Realiza cálculos com datas e horas, como encontrar a diferença entre duas datas ou adicionar um intervalo de tempo a uma data.

sqlalchemy import or_
Propósito: Importa a função or_ do módulo SQLAlchemy.
Funcionalidades:
Consultas lógicas: Permite criar consultas SQL complexas usando a expressão lógica OU.
Filtros: É usada para filtrar resultados de consultas com base em múltiplas condições.
