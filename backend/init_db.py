import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Cria a tabela de carros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            brand TEXT NOT NULL,
            price REAL NOT NULL,
            personality_type TEXT NOT NULL, -- Ex: "Aventureiro", "Economico", "Esportivo", "Luxo"
            description TEXT
        )
    ''')

    # Limpa os dados antigos para evitar duplicação em cada execução
    cursor.execute('DELETE FROM cars')

    # Dados de exemplo para o Tarnished_Lucy testar
    sample_cars = [
        ('Uno Mille', 'Fiat', 15000, 'Economico', 'Para quem tem o orçamento apertado, mas precisa ir de A para B com escada no teto.'),
        ('Gol Quadrado', 'Volkswagen', 20000, 'Aventureiro', 'Clássico! Agüenta qualquer tranco e a manutenção é barata.'),
        ('Civic', 'Honda', 90000, 'Esportivo', 'Para quem gosta de design agressivo e conforto.'),
        ('Range Rover', 'Land Rover', 400000, 'Luxo', 'Para quem quer conforto extremo e status (e não se preocupa com manutenção).'),
        ('Kwid', 'Renault', 45000, 'Economico', 'O SUV dos compactos, ideal para quem precisa de um carro novo sem gastar uma fortuna.'),
    ]

    cursor.executemany('''
        INSERT INTO cars (model, brand, price, personality_type, description)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_cars)

    conn.commit()
    conn.close()
    print("Banco de dados 'database.db' inicializado com sucesso com dados de exemplo!")

if __name__ == '__main__':
    init_db()
