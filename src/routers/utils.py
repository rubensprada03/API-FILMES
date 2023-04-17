from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from fastapi import FastAPI, Depends
from src.infra.providers import token_provider

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)):
    pass
