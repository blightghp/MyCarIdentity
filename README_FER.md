# Fala, Tarnished_Lucy! Tudo beleza?

Aqui é o Fer, e eu montei esse projeto com muito carinho pra você dar os primeiros passos de verdade no mundo da programação. Nada de tutorial genérico de TODO list — a gente vai aprender construindo algo que você curte: **carros**.

Eu sei que você quer aprender **TypeScript/JavaScript, Python, SQL, Git e terminal (PowerShell/Bash)**. Então juntei tudo num projeto só. Quando terminar isso aqui, você vai ter tocado em praticamente tudo que um dev junior precisa saber.

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

### Se você é COMPLETAMENTE iniciante:
1. Leia o `ARQUITETURA.md` inteiro. Sem pressa, com calma. Esse documento explica tudo.
2. Aprenda a usar o terminal (PowerShell): `cd`, `ls` (ou `dir`), `mkdir`, `cat`.
3. Aprenda Git básico: `git status`, `git add .`, `git commit -m "mensagem"`, `git push`.
4. Rode o backend e o frontend pra ver funcionando. Brinque com o Swagger UI.
5. Abra o `database.py` e tente entender o SQL ali dentro.

### Se você já sabe o básico:
1. Leia o `ARQUITETURA.md`, foque na Seção 6 (Motor de Recomendação) e Seção 7 (Roadmap).
2. Reescreva o `App.tsx` pra integrar os componentes (`QuizForm`, `ResultPanel`).
3. Rode o quiz completo e veja o resultado chegando do backend.
4. Melhore o algoritmo do `recommender.py` — ele tá funcional mas bem basicão.

### Ordem recomendada de estudo (o que eu faria no seu lugar):
```
1º  Terminal / PowerShell / Bash
2º  Git (add, commit, push, branch, merge)
3º  SQL (SELECT, INSERT, WHERE, JOIN)  ← brinque no database.db
4º  Python básico (variáveis, funções, listas, dicts)
5º  FastAPI (rotas, modelos, Swagger)
6º  TypeScript (tipos, interfaces, genéricos)
7º  React (componentes, useState, useEffect, fetch)
8º  CSS (flexbox, grid, variáveis, responsivo)
```

---

## 🔧 Recursos e onde pesquisar

| O que estudar                        | Onde ir                                        |
|--------------------------------------|------------------------------------------------|
| Python básico                        | https://docs.python.org/pt-br/3/tutorial/      |
| FastAPI (tutorial oficial, perfeito)  | https://fastapi.tiangolo.com/tutorial/          |
| SQL do zero                          | https://www.w3schools.com/sql/                  |
| React (doc oficial, atualizada)      | https://react.dev/learn                         |
| TypeScript                           | https://www.typescriptlang.org/docs/handbook/   |
| Git pra iniciante                    | https://learngitbranching.js.org/               |
| Preços de carro (FIPE)              | https://veiculos.fipe.org.br/                   |
| API FIPE gratuita                    | https://brasilapi.com.br/docs#tag/FIPE          |
| Datasets de carros (Kaggle)          | Procure "brazil cars dataset" no kaggle.com     |
| Notas de segurança                   | https://www.latinncap.com/                      |
| CSS Flexbox (jogo divertido)         | https://flexboxfroggy.com/                      |
| CSS Grid (outro jogo)               | https://cssgridgarden.com/                      |

---

## 🎯 Seus desafios (por ordem de dificuldade)

1. **[Fácil]** Rode o backend e use o Swagger UI pra listar os carros. Copie a resposta JSON e cole num arquivo `.json` pra estudar a estrutura.

2. **[Fácil]** Adicione 5 carros novos no `database.py` (pesquise preços reais na FIPE).

3. **[Médio]** Reescreva o `App.tsx` pra mostrar o `QuizForm` e, quando o quiz terminar, mostrar o `ResultPanel`.

4. **[Médio]** No `recommender.py`, melhore a geração de `justificativa` — em vez de um texto genérico, explique POR QUE aquele carro combina (ex: "Seu perfil econômico casa com o custo-benefício nota 5 do Onix").

5. **[Difícil]** Implemente o passo 4 do quiz (Prioridades) com checkboxes bonitos, onde o usuário arrasta pra ordenar por importância.

6. **[Difícil]** Adicione gráficos (pode usar a lib `recharts`) comparando os carros recomendados em radar chart (segurança vs conforto vs desempenho vs custo-benefício).

7. **[Boss Fight]** Integre com a API da FIPE (BrasilAPI) pra puxar preços atualizados automaticamente, em vez de ter tudo hardcoded no banco.

---

## 💡 Dicas de ouro

- **Não tente fazer tudo de uma vez.** Vai por etapas, segue o roadmap do `ARQUITETURA.md`.
- **Commite sempre.** Fez uma feature funcionar? `git add . && git commit -m "Adiciona filtro por categoria"`. Não espera acumular.
- **Usa branches.** Nunca code direto na `main`. Cria uma branch: `git checkout -b feat/minha-feature`.
- **Quando travar, lê o erro.** 90% dos bugs estão na mensagem de erro. Lê com calma, pesquisa no Google/StackOverflow.
- **O Swagger UI é seu melhor amigo.** Testa os endpoints lá antes de tentar chamar pelo frontend.

---

Bora, Tarnished_Lucy! A garagem tá aberta, as ferramentas estão na mesa. Agora é contigo. 🔧🏎️💨

— Fer
