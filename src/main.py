from fastapi import FastAPI, Depends
from src.schemas.schemas import Filmes, Usuario, FilmeSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_filme import RepositorioFilme
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware


#criar_bd()
app = FastAPI()

origins = ['http://localhost:3000',
          'http://myapp.vercel.com']
# CORS
app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# CRIAR FILME
@app.post('/filmes')
def criar_filmes(filme: Filmes, db: Session = Depends(get_db)):
    filme_criado = RepositorioFilme(db).criar(filme)
    return filme_criado

# LISTAR FILME
@app.get('/filmes', response_model=List[Filmes])
def listar_filmes( db: Session = Depends(get_db)):
    filmes = RepositorioFilme(db).listar()
    return filmes


# OBTER FILME
@app.get('/filmes/{filme_id}')
def obter_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = RepositorioFilme(db).obter(filme_id)
    return filme 

# DELETAR FILME
@app.delete('/filmes/{filme_id}')
def remover_filme(filme_id: int, db:Session = Depends(get_db)):
    RepositorioFilme(db).remover(filme_id)
    return{"msg": "Filme removido com sucesso"}

# ATUALIZAR FILME   
@app.put('/filmes/{id}')
def atualizar_produto(id:int, filme: Filmes, session: Session = Depends(get_db)):
    RepositorioFilme(session).editar(id, filme)
    return {"msg":"produto atualizado"}, filme

# CRIAR USUARIO 
@app.post('/usuarios', response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

# LISTAR USUARIOS
@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios  

