from fastapi import FastAPI, Depends, HTTPException, status
from src.schemas.schemas import  Usuario, UsuarioSimples, LoginData
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from typing import  List
from src.routers.utils import obter_usuario_logado
from src.infra.providers import hash_provider, token_provider 

from fastapi import APIRouter

router = APIRouter()

# CRIAR USUARIO 
@router.post('/signup', response_model=UsuarioSimples)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_localizado =RepositorioUsuario(session).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Ja existe um usuario para esse telefone!')
    
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
    


@router.post('/token')
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estao incorretos!')
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estao incorretos!')
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return {'usuario': usuario, 'access_token': token}

@router.get('/me', response_model=UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario
