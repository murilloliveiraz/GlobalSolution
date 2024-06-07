# Backend Sustaintravel

Bem vindo (a) ao repositório oficial do backend do projeto Sustaintravel: conectando viajantes conscientes a destinos sustentáveis. Esse repositório contém o código fonte e instruções para rodar o backend do projeto.

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- MySQL Connector
- Azure host (para o banco de dados)

## Instruções

Para rodar o projeto, siga os seguintes passos:

1. Faça um clone desse repositório em sua máquina:
    ```
    git clone https://github.com/murilloliveiraz/GlobalSolution.git
    ```
2. Entre na pasta **Python**:
    ```
    cd GlobalSolution/Python
    ```
3. Instale o Python:

    https://www.python.org/downloads/

4. Instale o Pip, gerenciador de pacotes do Python:
    ```
    py -m ensurepip --default-pip
    ```

5. Instale o Flask:
    ```
    pip install Flask
    ```

6. Instale o MySQL Connector:
    ```
    pip install mysql-connector-python
    ```

7. Rode o projeto:
    ```
    py .\index.py
    ```

O servidor irá iniciar em ```http://127.0.0.1:5000```, onde você pode acessar a API.

## Rotas

```/``` : retorna uma mensagem de boas vindas e o link para a documentação (esse repositório).

```/viagens``` : retorna um JSON contendo todas as viagens do banco de dados. 

## Exemplo de retorno

```
{
    data: [
        {
            avaliacao_media: 3,
            id: 2,
            imagem: "https://i0.wp.com/viajandocommoises.com.br/wp-content/uploads/2020/12/IMG_20201219_134745-1.jpg?resize=1024%2C472&ssl=1",
            nome: "Diamantina - MG",
            preco: 329.99,
            qtd_dias: 2,
            qtd_noites: 2,
            tags: [
                [
                "Sustentável"
                ],
                [
                "Ecológico"
                ],
                [
                "Vegano"
                ]
            ]
        }
    ]
}
```

## Integrantes

- David Murillo de Oliveira Soares (RM 559078)
- Yasmin Gonçalves Coelho (RM 559147)
