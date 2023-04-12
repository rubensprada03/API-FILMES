from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List


class RepositorioAluguel():

    def __init__(self, session: Session):
        self.session = session
    
    def gravar_aluguel(self, aluguel: schemas.Aluguel):
        pass

    def buscar_por_id(self, id:int) -> models.Aluguel:
        pass

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int):
        pass

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int):
        pass