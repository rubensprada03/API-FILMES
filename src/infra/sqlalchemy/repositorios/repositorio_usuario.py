from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import  select

class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session =  session

    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario(nome = usuario.nome,
                                    senha = usuario.senha,
                                    telefone = usuario.telefone,
                                    )
        
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listar(self):
        usuario = self.session.query(models.Usuario).all()
        return usuario

    def obter_por_telefone(self, telefone) -> models.Usuario:
        query = select(models.Usuario).where(models.Usuario.telefone == telefone)
        return self.session.execute(query).scalars().first()


    def remover():
        pass