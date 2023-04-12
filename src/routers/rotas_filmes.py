from fastapi import APIRouter
from src.infra.sqlalchemy.repositorios.repositorio_filme import RepositorioFilme
from src.schemas.schemas import Filmes
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


# CRIAR FILME
@router.post('/filmes')
def criar_filmes(filme: Filmes, db: Session = Depends(get_db)):
    filme_criado = RepositorioFilme(db).criar(filme)
    return filme_criado
                                                     
# LISTAR FILME
@router.get('/filmes', response_model=List[Filmes])
def listar_filmes( db: Session = Depends(get_db)):
    filmes = RepositorioFilme(db).listar()
    return filmes


# OBTER FILME
@router.get('/filmes/{filme_id}')
def obter_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = RepositorioFilme(db).obter(filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail='ID inexistente, tente novamente.')
    return filme 

# DELETAR FILME
@router.delete('/filmes/{filme_id}')
def remover_filme(filme_id: int, db:Session = Depends(get_db)):
    RepositorioFilme(db).remover(filme_id)
    return{"msg": "Filme removido com sucesso"}

# ATUALIZAR FILME   
@router.put('/filmes/{id}')
def atualizar_filme(id:int, filme: Filmes, session: Session = Depends(get_db)):
    RepositorioFilme(session).editar(id, filme)
    return {"msg":"produto atualizado"}, filme