from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

engine = create_engine('sqlite:///colaboradores.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Programadores(Base):
    __tablename__ = 'programadores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)
    email = Column(String(40))

    def __repr__(self):
        return f'<Id: {self.id} - Programador: {self.nome}>'


class Habilidades(Base):
    __tablename__ = 'habilidades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40))

    def __repr__(self):
        return f'<Id: {self.id} - Habilidade: {self.nome}>'


class ProgramadorHabilidade(Base):
    __tablename__ = 'programador_habilidade'

    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programadores.id'))
    habilidade_id = Column(Integer, ForeignKey('habilidades.id'))

    programador = relationship('Programadores')
    habilidade = relationship('Habilidades')

    def __repr__(self):
        return f'<Programador: {self.programador.nome} - Habilidades: {self.habilidade.nome}'


def salvar(self):
    db_session.add(self)
    db_session.commit()


def deletar(self):
    db_session.delete(self)
    db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
