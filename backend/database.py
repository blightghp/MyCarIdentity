import sqlite3
import json
from typing import List

# TODO: depois mudar isso pra um orm de verdade tipo sqlalchemy
DB_NAME = "mycaridentity.db"

def get_connection():
    # cria conexao com o banco
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # pra retornar como dict
    return conn

def create_tables():
    # cria as tabelas no bd se nao existir
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT,
        marca TEXT,
        ano_fabricacao INTEGER,
        ano_modelo INTEGER,
        preco_fipe REAL,
        preco_mercado REAL,
        categoria TEXT,
        combustivel TEXT,
        cambio TEXT,
        manutencao_custo_mensal REAL,
        seguro_medio_anual REAL,
        consumo_cidade REAL,
        consumo_estrada REAL,
        nota_seguranca INTEGER,
        nota_conforto INTEGER,
        nota_desempenho INTEGER,
        nota_custo_beneficio INTEGER,
        imagem_url TEXT,
        descricao TEXT
    )
    ''')
    conn.commit()
    conn.close()

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # checa se ja tem dado, se tiver nao faz nada pra nao duplicar
    cursor.execute("SELECT COUNT(*) FROM carros")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # TODO: carregar isso de um csv ou api da fipe depois
    # por enquanto vai na mao mesmo, peguei uns valores meio por cima
    carros_iniciais = [
        ("Uno Mille Economy", "Fiat", 2013, 2013, 18500.0, 19000.0, "hatch", "flex", "manual", 150.0, 1200.0, 12.0, 15.0, 2, 2, 2, 5, "", "O rei dos populares. Manutenção barata demais e não quebra."),
        ("HB20 Sense", "Hyundai", 2022, 2022, 65000.0, 67000.0, "hatch", "flex", "manual", 300.0, 2500.0, 13.0, 14.5, 4, 3, 3, 4, "", "Bom pra cidade, econômico e tem um visual legalzinho."),
        ("Onix LT", "Chevrolet", 2023, 2023, 75000.0, 78000.0, "hatch", "flex", "manual", 320.0, 2600.0, 13.5, 16.0, 5, 3, 3, 4, "", "Campeão de vendas, bebe pouco e seguro."),
        ("Polo Highline", "Volkswagen", 2023, 2024, 105000.0, 108000.0, "hatch", "flex", "automatico", 450.0, 3500.0, 11.0, 14.0, 5, 4, 4, 3, "", "Hatch premium, anda bem mas é mais caro de manter."),
        ("Gol Trendline", "Volkswagen", 2018, 2018, 42000.0, 44000.0, "hatch", "flex", "manual", 250.0, 1800.0, 11.5, 13.5, 3, 2, 3, 4, "", "Clássico brasileiro, pau pra toda obra."),
        ("Mobi Like", "Fiat", 2021, 2022, 48000.0, 50000.0, "hatch", "flex", "manual", 200.0, 1700.0, 13.0, 15.0, 2, 2, 2, 4, "", "Pequeno, cabe em qualquer vaga. Pro dia a dia é ok."),
        ("Corolla XEi", "Toyota", 2020, 2021, 130000.0, 135000.0, "sedan", "flex", "automatico", 500.0, 4000.0, 10.0, 12.5, 5, 5, 4, 4, "", "O sedã dos tios, mas não quebra nunca. Revenda garantida."),
        ("Civic Touring", "Honda", 2021, 2021, 145000.0, 150000.0, "sedan", "gasolina", "automatico", 600.0, 4500.0, 11.0, 14.0, 5, 5, 5, 3, "", "Motor turbo, baita design. Pra quem quer ser esportivo e familiar."),
        ("Virtus Highline", "Volkswagen", 2022, 2023, 115000.0, 118000.0, "sedan", "flex", "automatico", 450.0, 3800.0, 11.0, 14.0, 5, 4, 4, 4, "", "Espaçoso, bom porta-malas e motor espertinho."),
        ("Versa Advance", "Nissan", 2023, 2023, 100000.0, 105000.0, "sedan", "flex", "automatico", 400.0, 3200.0, 11.5, 14.5, 4, 4, 3, 4, "", "Confortável demais, ótimo pro dia a dia e viagens curtas."),
        ("Cronos Drive", "Fiat", 2021, 2022, 68000.0, 70000.0, "sedan", "flex", "manual", 300.0, 2500.0, 12.0, 14.0, 3, 3, 3, 4, "", "Porta-malas gigante pra categoria, design legal."),
        ("T-Cross Highline", "Volkswagen", 2023, 2023, 145000.0, 150000.0, "suv", "flex", "automatico", 550.0, 4200.0, 10.5, 13.0, 5, 4, 5, 3, "", "SUV completão, anda muito com motor 1.4 turbo."),
        ("Creta Prestige", "Hyundai", 2020, 2021, 105000.0, 110000.0, "suv", "flex", "automatico", 450.0, 3800.0, 9.0, 11.0, 4, 5, 3, 3, "", "Muito conforto, mas bebe bem."),
        ("Compass Longitude", "Jeep", 2022, 2022, 160000.0, 165000.0, "suv", "flex", "automatico", 700.0, 5000.0, 9.5, 12.0, 5, 5, 4, 3, "", "SUV médio queridinho do Brasil, acabamento top."),
        ("Renegade Sport", "Jeep", 2019, 2019, 75000.0, 78000.0, "suv", "flex", "automatico", 600.0, 3500.0, 8.5, 10.5, 4, 4, 2, 3, "", "Bonitão, mas o porta-malas é meio triste e o 1.8 é meio manco."),
        ("Nivus Highline", "Volkswagen", 2022, 2022, 125000.0, 130000.0, "suv", "flex", "automatico", 500.0, 4000.0, 11.0, 13.5, 5, 4, 4, 4, "", "Design coupé irado, pegada mais esportiva pra um SUV compacto."),
        ("Kicks Advance", "Nissan", 2021, 2022, 95000.0, 98000.0, "suv", "flex", "automatico", 400.0, 3200.0, 11.5, 13.5, 4, 4, 3, 4, "", "Econômico e muito confortável pra cidade."),
        ("Strada Freedom", "Fiat", 2022, 2023, 98000.0, 102000.0, "pickup", "flex", "manual", 350.0, 3500.0, 11.0, 13.0, 4, 3, 3, 4, "", "Líder de mercado, guenta o tranco no trampo e no lazer."),
        ("Toro Volcano", "Fiat", 2022, 2022, 155000.0, 160000.0, "pickup", "diesel", "automatico", 800.0, 6000.0, 10.0, 13.0, 5, 4, 4, 3, "", "Pickup de quem mora em apartamento, mas é muito boa de dirigir."),
        ("Hilux SRV", "Toyota", 2020, 2021, 220000.0, 230000.0, "pickup", "diesel", "automatico", 1000.0, 8000.0, 9.0, 11.0, 5, 3, 4, 3, "", "O tratorzinho indestrutível. Pula um pouco sem peso atrás."),
        ("Saveiro Cross", "Volkswagen", 2021, 2022, 85000.0, 88000.0, "pickup", "flex", "manual", 400.0, 3000.0, 11.0, 13.0, 3, 3, 4, 3, "", "Esportiva e guenta carregar umas tralhas no fim de semana."),
        ("BMW 320i", "BMW", 2021, 2022, 250000.0, 260000.0, "luxo", "flex", "automatico", 1500.0, 12000.0, 9.5, 13.0, 5, 5, 5, 2, "", "Pra quem quer status e dar umas aceleradas de fim de semana."),
        ("Mustang Mach 1", "Ford", 2021, 2021, 480000.0, 500000.0, "esportivo", "gasolina", "automatico", 3000.0, 20000.0, 5.0, 8.0, 5, 4, 5, 1, "", "V8 clássico, só pra quem tem bala na agulha. Faz barulho e gasta pneu."),
        ("Kwid Zen", "Renault", 2020, 2021, 40000.0, 42000.0, "hatch", "flex", "manual", 200.0, 1500.0, 14.0, 15.5, 2, 2, 2, 4, "", "SUV dos compactos (risos). Bem de entrada mas resolve a vida."),
        ("Yaris Hatch", "Toyota", 2022, 2023, 90000.0, 95000.0, "hatch", "flex", "automatico", 350.0, 2800.0, 11.0, 13.0, 4, 4, 3, 4, "", "Hatch confiável, mecânica Toyota é paz de espírito.")
    ]

    for c in carros_iniciais:
        cursor.execute('''
            INSERT INTO carros (modelo, marca, ano_fabricacao, ano_modelo, preco_fipe, preco_mercado, 
            categoria, combustivel, cambio, manutencao_custo_mensal, seguro_medio_anual, consumo_cidade, 
            consumo_estrada, nota_seguranca, nota_conforto, nota_desempenho, nota_custo_beneficio, imagem_url, descricao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', c)
        
    conn.commit()
    conn.close()
