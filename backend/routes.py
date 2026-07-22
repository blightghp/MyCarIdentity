from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
import sqlite3
from models import Car, UserProfile, Recommendation
from database import get_connection
from recommender import CarRecommender

router = APIRouter()
recommender = CarRecommender()

def _get_carros_do_banco():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros")
    rows = cursor.fetchall()
    conn.close()
    
    # converte de sqlite3.Row pro pydantic
    return [Car(**dict(row)) for row in rows]

@router.get("/api/carros", response_model=List[Car])
def listar_carros(categoria: Optional[str] = None, preco_max: Optional[float] = None, marca: Optional[str] = None):
    # TODO: paginar isso aqui qnd a base crescer, se nao vai explodir a memoria
    carros = _get_carros_do_banco()
    
    # aplicando os filtros de padaria
    if categoria:
        carros = [c for c in carros if c.categoria.lower() == categoria.lower()]
    if preco_max:
        carros = [c for c in carros if c.preco_mercado <= preco_max]
    if marca:
        carros = [c for c in carros if c.marca.lower() == marca.lower()]
        
    return carros

@router.get("/api/carros/{id}", response_model=Car)
def pegar_carro(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Deu ruim, carro não encontrado")
        
    return Car(**dict(row))

@router.post("/api/recomendar", response_model=List[Recommendation])
def recomendar_carros(perfil: UserProfile):
    carros = _get_carros_do_banco()
    recs = recommender.recomendar(perfil, carros, top_n=5)
    
    # se não sobrar nenhum carro viavel pro cara
    if not recs:
        # TODO: talvez retornar uns carros mais baratos como alternativa
        return []
        
    return recs

@router.get("/api/marcas", response_model=List[str])
def listar_marcas():
    # pego as marcas unicas na marra
    carros = _get_carros_do_banco()
    marcas = list(set([c.marca for c in carros]))
    marcas.sort()
    return marcas

@router.get("/api/categorias", response_model=List[str])
def listar_categorias():
    carros = _get_carros_do_banco()
    categorias = list(set([c.categoria for c in carros]))
    categorias.sort()
    return categorias
