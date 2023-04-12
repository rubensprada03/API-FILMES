from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Filme(Base):

    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ator = Column(String)
    duracao = Column(Integer)
    genero = Column(String)
    ano = Column(Integer)
    nota = Column(Float)
    disponivel = Column(Boolean, default=False) 
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship('Usuario', back_populates='filmes')

class Usuario(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    filmes = relationship('Filme', back_populates='usuario')
    alugueis = relationship('Aluguel', back_populates='usuario')


class Aluguel(Base):

    __tablename__ = 'aluguel'

    id = Column(Integer, primary_key=True, index=True)
    compra = Column(Boolean, default=False)
    dias = Column(Integer)
    qualidade = Column(String)

    usuario_id = Column(Integer, ForeignKey('usuarios.id', name='fk_aluguel_usuario'))
    filme_id = Column(Integer, ForeignKey('filmes.id', name='fk_aluguel_filme'))


    usuario = relationship('Usuario', back_populates='alugueis')
    filme = relationship('Filme')
    
