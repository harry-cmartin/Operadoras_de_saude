# API de Operadoras de Saúde

Esta API foi desenvolvida com Django e Django REST Framework para geenciar uma busca textual para um arquivo csv.

## Estrutura do Projeto (MVC)

O projeto segue a arquitetura MVC (Model-View-Controller):

### Model (Modelo)
- `api/models.py`: Define o modelo `Operadora` com todos os campos necessários para armazenar os dados do CSV.

### View (Controlador no Django)
- `api/views.py`: Contém a lógica de negócios e manipulação de requisições.
-  Apenas operações de leitura (GET) e a funcionalidade de busca.

### Controller (View no Django)
- `api/urls.py`: Define as rotas da API.
- `operadoras_api/urls.py`: Configura as URLs do projeto.

### Outros componentes
- `api/serializers.py`: Converte objetos do modelo em JSON e vice-versa.
- `api/management/commands/import_operadoras.py`: Comando personalizado para importar dados do CSV.

## Funcionalidades

- **Listagem**: Retorna apenas os resultados da busca
- **Busca textual**: Permite buscar operadoras por texto em vários campos (registro_ans, razao_social, nome_fantasia, cidade, cnpj, representante, UF,modalidade, cep e regiao de comercialização).
- **Apenas leitura**: Suporta apenas operações de leitura (GET) .

## Configuração e Execução

1. Instale as dependecias:

   ```
   python -m pip install django djangorestframework django-cors-headers pandas django-filter

   ```

2. Execute as migrações:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Importe os dados do CSV:
   ```
   python manage.py import_operadoras Relatorio_cadop.csv
   ```

4. Inicie o servidor:
   ```
   python manage.py runserver
   ```

5. Acesse a API em: http://127.0.0.1:8000/api/operadoras/

## Endpoints da API

### GET /api/operadoras/
Lista todas as operadoras existentes.

### GET /api/operadoras/?search=texto
Busca até operadoras que contenham o texto informado em qualquer um dos campos (registro_ans, razao_social, nome_fantasia, cidade, cnpj, representante, UF,modalidade, cep e regiao de comercialização).

### GET /api/operadoras/{registro_ans}/
Retorna os detalhes de uma operadora específica pelo seu Registro ANS.

## Postman

Foi criada uma coleção do Postman para demosnstrar o resultado obtido com a construção. Para utilizá-la:

1. Abra o Postman
2. Clique em "File" -> "Import" -> Selecione o arquivo `Operadora_de_saude.postman_collection.json` presente na raiz dessa pasta
3. A coleção "Operadoras_de_saude" será importada com os seguintes endpoints:

- **Listar todas operadoras**: GET http://127.0.0.1:8000/api/operadoras/
- **Buscar operadoras por texto**: GET http://127.0.0.1:8000/api/operadoras/?search=SÃO%20PAULO
- **Obter operadora específica**: GET http://127.0.0.1:8000/api/operadoras/419761/



## Frontend

O frontend foi desenvolvido com Vue.js e se conecta à API Django. Para executar o frontend:

1. Inicie o servidor para o frontend:
   ```
   python serve_frontend.py
   ```

2. Acesse o frontend em: http://localhost:8080

3. Use o campo de busca para encontrar operadoras.
