# Leia tudo, Fer, seu N00b?

Preparei esse projetinho para você passar muita raiva e se divertir muito. 

Bom, vocêr quer aprender a base de **TypeScript/JavaScript, Python, Bancos de Dados (SQL/SQLite) e ferramentas como Git e PowerShell**, né? Então, já uni o útil ao agradável.

Bem-vindo ao **MyCarIdentity**! 🏎️

O app responde duas perguntas:
- *Qual carro reflete a minha personalidade?*
- *Com o que eu ganho, qual carro eu consigo ter de verdade?*

---

## 📂 O que tem em cada pasta (mapa do tesouro)

```
MyCarIdentity/
│
├── ARQUITETURA.md         ← O DOCUMENTO MAIS IMPORTANTE. Leia ANTES de mexer em qualquer coisa.
│                            Tem o roadmap completo, a explicação do algoritmo, o modelo de dados,
│                            tudo mastigado. Sério, leia esse primeiro.
│
├── README.md              ← Descrição curta do projeto (pro GitHub).
├── README_FER.md          ← ESTE ARQUIVO. Seu guia de sobrevivência.
├── .gitignore             ← Diz pro Git o que NÃO subir (node_modules, .venv, banco, etc).
│
├── backend/               ← O CÉREBRO do app (Python + FastAPI)
│   ├── main.py            ← Ponto de entrada. Sobe o servidor, configura CORS, registra as rotas.
│   ├── routes.py          ← Os endpoints da API (GET /api/carros, POST /api/recomendar, etc).
│   ├── models.py          ← Os "moldes" de dados. Define a estrutura de Car, UserProfile, Recommendation.
│   ├── database.py        ← Conexão com o SQLite, criação de tabelas e seed (dados iniciais).
│   ├── recommender.py     ← O MOTOR DE RECOMENDAÇÃO. A lógica que calcula qual carro combina contigo.
│   ├── init_db.py         ← Script antigo de seed (mantive pra referência, mas o database.py já faz isso).
│   ├── requirements.txt   ← Lista de pacotes Python que o projeto precisa.
│   ├── .venv/             ← Ambiente virtual Python (NÃO mexe aqui, NÃO commita).
│   └── *.db               ← Arquivo do banco SQLite (gerado automaticamente, NÃO commita).
│
└── frontend/              ← A CARA do app (React + TypeScript + Vite)
    ├── src/
    │   ├── main.tsx           ← Entry point do React (onde tudo começa).
    │   ├── App.tsx            ← Componente raiz (VOCÊ VAI REESCREVER esse cara).
    │   ├── App.css            ← Estilos do App (pra você estilizar).
    │   ├── index.css          ← Reset CSS global.
    │   │
    │   ├── types/
    │   │   └── index.ts       ← Interfaces TypeScript (Car, UserProfile, Recommendation).
    │   │                        Espelha os models do backend, mas em camelCase (padrão JS/TS).
    │   │
    │   ├── services/
    │   │   └── api.ts         ← Módulo que faz as chamadas HTTP pro backend.
    │   │                        Tem fetch com tratamento de erro, tudo tipado.
    │   │
    │   ├── components/
    │   │   ├── QuizForm.tsx   ← Formulário multi-step (5 etapas) do quiz de personalidade.
    │   │   ├── CarCard.tsx    ← Componente visual de card de um carro (imagem, preço, badges).
    │   │   └── ResultPanel.tsx← Painel que mostra as recomendações com score e parcela estimada.
    │   │
    │   └── styles/
    │       └── variables.css  ← Variáveis CSS globais (cores, fontes, espaçamentos).
    │                            Dark theme com cores inspiradas em painel de carro à noite.
    │
    ├── package.json           ← Dependências do frontend (React, TypeScript, Vite).
    ├── tsconfig.json          ← Configuração do TypeScript.
    └── vite.config.ts         ← Configuração do Vite (build tool).
```

---

## 🚀 Como rodar esse bagulho

### Pré-requisitos
Você precisa ter instalado:
- **Node.js** (versão 18+) → `node --version` pra checar
- **Python** (versão 3.10+) → `python --version` pra checar
- **Git** → `git --version` pra checar

### Backend (o servidor Python)
```powershell
# 1. Entra na pasta do backend
cd backend

# 2. Ativa o ambiente virtual (SEMPRE fazer isso antes de rodar qualquer coisa Python)
.\.venv\Scripts\activate    # Windows (PowerShell)
# source .venv/bin/activate  # Linux/Mac (Bash)

# 3. Se for a primeira vez, instala as dependências
pip install -r requirements.txt

# 4. Roda o servidor
uvicorn main:app --reload

# 5. Abre no navegador: http://127.0.0.1:8000/docs
#    Essa página (Swagger UI) lista todos os endpoints e deixa testar na hora!
```

### Frontend (o site React)
```powershell
# 1. Entra na pasta do frontend (em outro terminal!)
cd frontend

# 2. Se for a primeira vez depois de clonar, instala as dependências
npm install

# 3. Roda o servidor de desenvolvimento
npm run dev

# 4. Abre no navegador: http://localhost:5173
```

> ⚠️ **Os dois servidores precisam estar rodando ao mesmo tempo!** Backend numa janela do terminal, frontend em outra.

---

## 📖 Por onde começar a estudar

Mãos à obra O mundo da programação é quebrar a cabeça até funcionar. Eu acredito em você, agora vai lá e faz esse app de carros rodar! 🏎️💨
