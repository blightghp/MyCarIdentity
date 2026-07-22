from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from database import create_tables, seed_data

# cria a instancia do app
app = FastAPI(
    title="MyCarIdentity API",
    description="API do MyCarIdentity - descubra qual carro combina com vc",
    version="0.1.0"
)

# libera o cors pro frontend conseguir chamar a api sem dar erro maluco
# TODO: em produção limitar as origins direito
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registra as rotas
app.include_router(router)

# inicializa o banco quando o servidor sobe
@app.on_event("startup")
def startup_event():
    create_tables()
    seed_data()
    print("banco de dados pronto e populado!")

@app.get("/")
def read_root():
    return {"message": "Fala! Bem-vindo à API do MyCarIdentity 🏎️"}
