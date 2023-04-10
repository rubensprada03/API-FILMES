from pydantic import BaseModel
from typing import Optional, List

class FilmeSimples(BaseModel):
    id: Optional[str] = None
    nome:str
    ano: float

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int]
    nome: str
    telefone: str
    senha: str
    filmes: List[FilmeSimples] = []

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class Filmes(BaseModel):
    id: Optional[int] = None
    nome: str
    ator: str
    duracao: int
    genero: str
    ano: int
    nota: float
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

