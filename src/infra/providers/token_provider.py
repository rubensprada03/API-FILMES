from jose import jwt
from datetime import datetime, timedelta

# CONFIG
SECRET_KEY = '85EE0FE4F155A9AF2657D85054AD63CA'
ALGORITHM = 'HS256'
EXPIRE_IN_MIN = 3000

def criar_access_token(data: dict):
    dados = data.copy()
    experiracao = datetime.utcnow() + timedelta(minutes=EXPIRE_IN_MIN)
    dados.update({'exp': experiracao})
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token: str):
    carga =  jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')
