# API - Cadastro de desenvolvedores
---

Este projeto é uma API que realiza o cadastro de desenvolvedores 
e suas habilidades. Nesta API é possível realizar o CRUD das seguintes
entidades: Programador, Habilidade e Colaborador. 

### Ambiente
Para reproduzir o ambinete para execução deste projeto basta 
criar um ambiente virtual e executar o arquivo *requirements.txt*:
```python
python3 -m venv nomedoambientevirtual
source nomedoambientevirtual/bin/activate
pip install requirements.txt
``` 
É importante ressaltar que as configurações apresentadas neste tópico
são feitas para o sistema operacional Linux. Para mais informações sobre
ambientes virtuais: https://docs.python.org/pt-br/3/library/venv.html

### Formato para requisições (*requests*) e respostas (*responses*)
Esta API recebe e retorna informações no formato JSON 
(JavaScript Object Notation - https://pt.wikipedia.org/wiki/JSON). O JSON
possui o formato de chave e valor para seus elementos, o tópico de
`Exemplos` mostrará como realizar ações dentro da API. 

### Base de dados
O ORM utilizado para construir a base de dados deste projeto
é o SQLALCHEMY, com ele é possível criar tableas a partir de 
classes em python, além de oferecer outras funções que permitem
realiza ações equivalentes a comandos SQL. O banco de dados utilizado
neste projeto é o SQLITE, mas o SQLALCHMEY se comunica com outros 
bancos de dados relacionais. Os arquivos *models.py* e *utils.py*
contem as configuraçoes necessarias para a criaçao da base dados.
Para criar a base de dados, basta executar os seguintes comandos:

```python
python3 models.py
python3 utils.py
```

O arquivo *models.py* contém as informações para a criação das tebelas
**Programadores**, **Habilidadades** e **ProgrmadorHabilidade** que une as 
informações das tabelas Programadores e Habilidades. 

### Classes 
Além da classes para a criação das tabelas da base de dos
(contidas no arquivo *models.py*) há outras dois arquivos 
(*Habilidade.py, Programador.py* e *Colaborador.py* 
representado ProgramadorHabilidade) que contém as funções para inserção, consulta, alteração e
deleção de programadores e habilidades. As ações desta
API estão divididas em classes por conta da da utilização 
da biblioteca flask-restful, para mais informações acesse: https://flask-restful.readthedocs.io/en/latest/.
Os atributos da classes (***definido em models.py***) Habilidade, Programador e Colaborador, estão descritos abaixo:

- Classe Programador

    - id (gerado automaticamente)
    - nome
    - idade
    - email
    
- Habilidades
    
    - id (garado automaticamente)
    - nome
    
- Colaborador

    - id (gerado automaticamente)
    - programador (chave estrangeira de programador)
    - habilidade (chave estrangeira de habilidadae)
    
Em cada classe modelada em **models.py** há uma função *def__rep__()* que retorna em formato de string
informações inseridas na base de dados. Se necessário, é possível criar novos *scripts* em *utils.py* e 
assim visualizar outras informações inseridas na base de dados. * Observação: às vezes é necessário
realizar um *drop base* na base de dados para testar novos resultados.
    

### Execução da aplicação

O arquivo *app.py* contém a função principal para execução 
do projeto, além da função principal também há as rotas para
acesso aos recursos da API. Para executar o projeto:

```python
python3 app.py
```

*Observação: para executar o projeto (no mode *debug*) conforme a recomendação 
do projeto oficial do Flask: 
```python
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

### Rotas
As rotas fornecidas nesta API permite a utilização dos recursos,
inserindo corretamente os parâmetros de rotas é possível visualizar 
os resultados utilizando ferramentas REST Client como
Postman (https://www.postman.com/), Insomnia (https://insomnia.rest/) 
ou o navegador (Chrome, Firefox, etc). Para utilizar um recurso basta digitar 
no navegador: **localhost:5000/nomedorecurso**, a porta 5000 é a 
porta padrão utilizada pelo Flask, para mais informações é
só acessar a documentação oficial.

*Observação: a barra ( / ) ao final de cada rota deve ser inserida, caso contrário, o 
recurso não será utilizado. 
 
---
Rotas para recursos de programador:

- `/consultar_programador/<int:id>/`
- `/deletar_programador/<int:id>/`
- `/atualizar_programador/<int:id>/`
- `/cadastrar_programador/`

Com exceção `cadastrar_progrmador`, todos os recursos precisam de um `id` (inteiro),
caso seja inserido um dado (string, etc) diferente de um numero inteiro,
um erro será emitido ao usuário informando que a rota não existe.

---
Rotas para recursos de habilidade:

- `/consultar_habilidade/<int:id>/`
- `/atualizar_habilidade/<int:id>/`
- `/deletar_habilidade/<int:id>/`
- `/cadastrar_habilidade/`

Os parâmetros rotas (`id`) de Habilidades, também, utilizam somente números inteiros 
(exceto `cadastrar_habilidade`) e caso outro tipo de dado seja inserido, 
um erro de rota não encontrada será apresentado. 

---
Rotas para colaborador

- `/consultar_colaborador/<int:id>/`
- `/atualizar_colaborador/<int:id>/`
- `/deletar_colaborador/<int:id>/`
- `/cadastrar_colaborador/`

Os recursos de colaboradores permitem realizar operações 
com outras entidades (Programador e Habilidade), os parâmetros
de rotas (`id`) aceitam somente números inteiros, aprensetando um erro
caso o *id* seja *string* e etc.

---
Rotas de listagem de dados:

- `/lista_prgramadores/`
- `/lista_habildades/`
- `/lista_colaboradores/`

Estes recursos listam os todos os dados cadastrados na base de dados.

### Exemplos
Abaixo segue alguns exemplos sobre como cadastrar um usuario:

```json
{
	"nome": "p5",
	"idade": 18,
	"email": "p5@gmail.com"
}
```

Atualizar usuário, lembrando o `id` do usuário para atualização deve ser passado
na rota:
```json
{
	"nome": "p5",
	"idade": 18,
	"email": "p5@gmail.com"
}
``` 
Para atualizar dados, não é necessário inserir todos os campos. Para outras operações, de consulta,
deleção e listagem, basta utilizar um *id* cadastrado no resultado e visualizar o resultado em um
*rest client* ou no navegador. 




