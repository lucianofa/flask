from flask_restful import Resource
from models import *
from flask import request


class Habilidade(Resource):

    def get(self, id):
        try:
            habilidade = Habilidades.query.get(id)
            response = {
                'id': habilidade.id,
                'nome': habilidade.nome
            }
        except AttributeError:
            response = {
                'mensagem': 'Id não encontrado na base de dados'
            }
        return response

    def put(self, id):
        try:
            habilidade = Habilidades.query.get(id)
            nova_habilidade = request.json

            if 'nome' in nova_habilidade:
                habilidade.nome = nova_habilidade['nome']

            salvar(habilidade)

            response = {
                'id': habilidade.id,
                'nome': habilidade.nome,
            }
            print(response)
        except AttributeError:
            response = {
                'mensagem': 'Id não encontrado'
            }

        return response

    def delete(self, id):
        try:
            habilidade = Habilidades.query.get(id)
            deletar(habilidade)
            response = {
                'mensagem': 'Habilidade deletada com sucesso'
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
        habilidade = request.json
        nova_habilidade = Habilidades(nome=habilidade['nome'])
        salvar(nova_habilidade)
        response = {'mensagem': 'Habilidade inserido com sucesso'}
        return response


class ListaHabilidades(Resource):
    def get(self):
        habilidades = Habilidades.query.all()
        response = [
            {'id': i.id, 'nome': i.nome}
            for i in habilidades
        ]

        return response