from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do MyCarIdentity, Tarnished_Lucy!"}

@app.get("/cars")
def get_cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return [dict(car) for car in cars]

# Desafio: criar um endpoint /recommend que receba a renda e a personalidade do usuário e sugira um carro!
