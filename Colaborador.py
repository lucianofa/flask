from flask_restful import Resource
from models import *
from flask import request


class Colaborador(Resource):

    def post(self):
        colaborador = request.json
        try:
            programador = Programadores.query.get(colaborador['programador_id'])
            habilidade = Habilidades.query.get(colaborador['habilidade_id'])
            novo_colaborador = ProgramadorHabilidade(
                programador_id=programador.id,
                habilidade_id=habilidade.id
            )
            salvar(novo_colaborador)
            response = {
                'mensagem': 'Colaborador cadastrado'
            }
        except AttributeError:
            response = {
                'mensagem': 'Verificar Atributos'
            }
        except Exception:
            response = {
                'mensagem': 'Erro Interno'
            }

        return response

    def get(self, id):
        try:
            colaborador = ProgramadorHabilidade.query.get(id)
            response = {
                'programador_id': colaborador.programador_id,
                'nome': colaborador.programador.nome,
                'habilidade_id': colaborador.habilidade_id,
                'habilidade': colaborador.habilidade.nome
            }
        except AttributeError:
            response = {
                'mensagem': 'Id nao encontrado na base de dados'
            }
        except Exception:
            response = {
                'mensagem': 'Erro Interno'
            }

        return response

    def put(self, id):
        novo_colaborador = request.json

        try:
            colaborador = ProgramadorHabilidade.query.get(id)

            if 'programador_id' in novo_colaborador:
                novo_programador = Programadores.query.get(
                    novo_colaborador['programador_id']
                )
                print(novo_programador.id)
                colaborador.programador_id = novo_programador.id

            if 'habilidade_id' in novo_colaborador:
                nova_habilidade = Habilidades.query.get(
                    novo_colaborador['habilidade_id']
                )
                colaborador.habilidade_id = nova_habilidade.id

            salvar(colaborador)

            response = {
                'programador_id': colaborador.programador_id,
                'nome': colaborador.programador.nome,
                'habilidade_id': colaborador.habilidade_id,
                'habilidade': colaborador.habilidade.nome
            }

        except AttributeError:
            response = {
                'mensagem': 'Verifique o Id novamente'
            }
        except Exception:
            response = {
                'mensagem': 'Erro Interno'
            }

        return response

    def delete(self, id):
        try:
            colaborador = ProgramadorHabilidade.query.get(id)
            deletar(colaborador)
            response = {
                'mensagem': 'Colaborador excluído com sucesso'
            }
        except IndexError:
            response = {
                'mensagem': 'Id não encontrador'
            }
        except Exception:
            response = {
                'mensagem': 'Erro interno'
            }
        return response


class Colaboradores(Resource):
    def get(self):
        colaboradores = ProgramadorHabilidade.query.all()
        response = [
            {
                'programador_id': c.programador.id,
                'nome': c.programador.nome,
                'habilidade_id': c.habilidade.id,
                'habilidade': c.habilidade.nome
            }
            for c in colaboradores
        ]
        return response