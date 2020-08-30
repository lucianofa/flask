from models import *


def inserir_programador():
    p1 = Programadores(nome='Pablo', idade=23, email='p1@gmail.com')
    p2 = Programadores(nome='Henrique', idade=22, email='p2@gmail.com')
    p3 = Programadores(nome='Sousa', idade=21, email='p3@gmail.com')

    salvar(p1)
    salvar(p2)
    salvar(p3)

    return f'Programadores inseridos'


def consultar_programador():
    programadores = Programadores.query.all()
    return programadores


def inserir_habilidade():
    h1 = Habilidades(nome='Front-end')
    h2 = Habilidades(nome='Back-end')
    h3 = Habilidades(nome='IA')

    salvar(h1)
    salvar(h2)
    salvar(h3)

    return f'Habilidades Inseridas'


def consultar_habilidade():
    habilidades = Habilidades.query.all()
    return habilidades


def inserir_colaborador():
    c1 = ProgramadorHabilidade(programador_id=1, habilidade_id=2)
    salvar(c1)
    return f'Colaborador inserido'


def consultar_colaborador():
    colaboradores = ProgramadorHabilidade.query.all()
    colaboradores = ProgramadorHabilidade.query.get(1)
    return colaboradores

if __name__ == '__main__':
    print('Inserindo programadores na base de dados:\n -->', inserir_programador())
    print('Inserindo habilidades na base de dados:\n -->', inserir_habilidade())
    print('\nConsultando programadores na base de dados:\n -->', consultar_programador())
    print('Consultando habilidades na base de dados:\n -->', consultar_habilidade())

    print(inserir_colaborador())
    print(consultar_colaborador())