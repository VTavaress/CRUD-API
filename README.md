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
