from pydantic import BaseModel, Field
from typing import List, Optional

# modelos de dados pra API
# TODO: usar sqlalchemy depois se a gente for pra um bd mais robusto (postgres)

class Car(BaseModel):
    id: Optional[int] = None
    modelo: str
    marca: str
    ano_fabricacao: int
    ano_modelo: int
    preco_fipe: float
    preco_mercado: float
    categoria: str # hatch, sedan, suv, pickup, esportivo, luxo
    combustivel: str
    cambio: str # manual ou automatico
    manutencao_custo_mensal: float
    seguro_medio_anual: float
    consumo_cidade: float
    consumo_estrada: float
    nota_seguranca: int = Field(ge=1, le=5)
    nota_conforto: int = Field(ge=1, le=5)
    nota_desempenho: int = Field(ge=1, le=5)
    nota_custo_beneficio: int = Field(ge=1, le=5)
    imagem_url: Optional[str] = None
    descricao: Optional[str] = None

class UserProfile(BaseModel):
    nome: str
    renda_mensal: float
    valor_entrada: float
    parcelas_max: int
    personalidade: str # aventureiro, conservador, esportivo, economico, status
    prioridades: List[str] # seguranca, economia, conforto, desempenho, estetica
    uso_principal: str # cidade, estrada, misto

class Recommendation(BaseModel):
    car: Car
    score: float
    justificativa: str
    parcela_estimada: float
    comprometimento_renda_pct: float
