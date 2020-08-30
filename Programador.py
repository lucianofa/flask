from flask import request
from flask_restful import Resource
from models import *


class Programador(Resource):
    def get(self, id):
        try:
            programador = Programadores.query.get(id)
            response = {
                'id': programador.id,
                'nome': programador.nome,
                'idade': programador.idade,
                'email': programador.email
            }
        except AttributeError:
            response = {
                'mensagem': 'Id não encontrado na base de dados'
            }
        return response

    def put(self, id):
        try:
            programador = Programadores.query.get(id)
            novo_programador = request.json

            if 'nome' in novo_programador:
                programador.nome = novo_programador['nome']
            if 'idade' in novo_programador:
                programador.idade = novo_programador['idade']
            if 'email' in novo_programador:
                programador.email = novo_programador['email']

            salvar(programador)

            response = {
                'id': programador.id,
                'nome': programador.nome,
                'idade': programador.idade
            }

        except AttributeError:
            response = {
                'mensagem': 'Id não encontrado'
            }

        return response

    def delete(self, id):
        try:
            programador = Programadores.query.get(id)
            deletar(programador)
            response = {
                'mensagem': 'Usuário deletado com sucesso'
            }
        except IndexError:
            response = {
                'mensagem': 'Id não encontrado'
            }

        except Exception:
            response = {
                'mensagem': 'Erro interno'
            }

        return response

    def post(self):
        programador = request.json
        novo_programador = Programadores(
            nome=programador['nome'],
            idade=programador['idade'],
            email=programador['email']
        )
        salvar(novo_programador)
        response = {
            'mensagem': 'usuário inserido com sucesso'
        }
        return response


class ListaProgramadores(Resource):

    def get(self):
        programadores = Programadores.query.all()
        response = [
            {'id': i.id, 'nome': i.nome, 'idade': i.idade, 'email': i.email}
            for i in programadores
        ]

        return response
