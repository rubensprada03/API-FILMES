from fastapi import FastAPI, Depends
from src.routers import rotas_auth
from src.infra.sqlalchemy.config.database import get_db
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_filmes, rotas_pedidos, rotas_auth


app = FastAPI()

origins = ['http://localhost:3000',
          'http://myapp.vercel.com']
# CORS
app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# ROTAS FILMES
app.include_router(rotas_filmes.router)

# SEGURANÇA
app.include_router(rotas_auth.router, prefix="/auth")

# ROTAS PEDIDOS 
app.include_router(rotas_pedidos.router)
