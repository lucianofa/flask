from flask import Flask
from flask_restful import Api
from Programador import *
from Habilidade import *
from Colaborador import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Programador,
                 '/consultar_programador/<int:id>/',
                 '/atualizar_programador/<int:id>/',
                 '/deletar_programador/<int:id>/',
                 '/cadastrar_programador/'
                 )
api.add_resource(Habilidade,
                 '/consultar_habilidade/<int:id>/',
                 '/atualizar_habilidade/<int:id>/',
                 '/deletar_habilidade/<int:id>/',
                 '/cadastrar_habilidade/'
                 )
api.add_resource(ListaProgramadores, '/listar_programadores/')
api.add_resource(ListaHabilidades, '/listar_habilidades/')
api.add_resource(Colaborador,
                 '/cadastrar_colaborador/',
                 '/consultar_colaborador/<int:id>/',
                 '/alterar_colaborador/<int:id>/',
                 '/deletar_colaborador/<int:id>/'
                 )
api.add_resource(Colaboradores, '/listar_colaboradores/')

if __name__ == '__main__':
    app.run(debug=True)
