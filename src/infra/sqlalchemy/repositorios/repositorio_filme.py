from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select, delete
from sqlalchemy import update

class RepositorioFilme():
    def __init__(self, db: Session):
        self.session = db

    def criar(self, filme: schemas.Filmes):
        session_filme = models.Filme(nome = filme.nome,
                                ator = filme.ator,
                                duracao = filme.duracao,
                                genero = filme.genero,
                                ano = filme.ano,
                                nota = filme.nota,
                                usuario_id = filme.usuario_id
                                )
        
        self.session.add(session_filme)
        self.session.commit()
        self.session.refresh(session_filme)
        return session_filme    
    
    def listar(self):
        filmes = self.session.query(models.Filme).all()
        return filmes
    
    def obter(self, filme_id: int):
        filme = self.session.query(models.Filme).filter(models.Filme.id == filme_id).first()
        return filme

    def remover(self, filme_id: int):
        stmt = delete(models.Filme).where(models.Filme.id == filme_id)

        self.session.execute(stmt)
        self.session.commit()

    def editar(self,id:int, filme: schemas.Filmes):
        update_stmt = update(models.Filme).where(models.Filme.id == id).values(nome = filme.nome,
                                                                                    ator = filme.ator,
                                                                                    duracao = filme.duracao,
                                                                                    genero = filme.genero,
                                                                                    ano = filme.ano,
                                                                                    nota = filme.nota,
                                                                                    )
        self.session.execute(update_stmt)
        self.session.commit()