from src.infra.sqlalchemy.config.database import get_db
from fastapi import FastAPI, Depends
from typing import  List
from sqlalchemy.orm import Session
from fastapi import APIRouter
from src.schemas.schemas import Aluguel 
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioAluguel


router = APIRouter()

@router.post('/pedidos')
def fazer_pedido(aluguel: Aluguel, session: Session = Depends(get_db)):
    aluguel_criado = RepositorioAluguel(session).gravar_aluguel(aluguel)
    return aluguel_criado

@router.get('/pedidos/{id}')
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    aluguel = RepositorioAluguel(session).buscar_por_id(id)
    return aluguel

@router.get('/pedidos')
def listar_pedidos(usuario_id:int ,session: Session = Depends(get_db)):
    alugueis = RepositorioAluguel(session).listar_meus_pedidos_por_usuario_id(usuario_id)
    return alugueis

@router.get('/pedidos/{usuario_id}/vendas')
def listar_vendas(usuario_id:int ,session: Session = Depends(get_db)):
    alugueis = RepositorioAluguel(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return alugueis

