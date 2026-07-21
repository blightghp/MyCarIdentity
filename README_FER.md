# Fala, Tarnished_Lucy! Tudo beleza?

Aqui é o seu tio (ou sua tia, sabe como é, a gente faz de tudo pra ver você voar!), e eu preparei esse projetinho com muito carinho para você dar os primeiros passos no mundo da programação, já botando a mão na massa com coisas que o mercado usa de verdade. 

Eu sei que você curte muito carros e quer aprender a base de **TypeScript/JavaScript, Python, Bancos de Dados (SQL/SQLite) e ferramentas como Git e PowerShell**. Então, a gente uniu o útil ao agradável! 

Bem-vindo ao **MyCarIdentity**! O objetivo desse app (que você vai construir quase todo) é responder a pergunta: *Qual carro reflete a sua personalidade?* E mais: *Com base na minha renda e capacidade de investimento, qual carro combina comigo?*

Eu deixei uma base mastigada aqui para você não começar do zero absoluto, mas o "grosso" do trabalho é seu. Bora ver o que tem na garagem?

---

## 🚗 O que eu deixei preparado para você (Arquitetura do Projeto)

Se você olhar as pastas aqui, vai ver que eu dividi o projeto em duas partes clássicas: o **Frontend** (a cara do app) e o **Backend** (o cérebro do app).

### 1. A pasta `/frontend`
Aqui está o código visual do seu site.
- **Tecnologia:** React com TypeScript.
- **Por que isso?** React é a biblioteca mais famosa do mundo para criar interfaces. E o TypeScript vai te ensinar a criar um código forte, tipado, que não quebra à toa (você disse que queria aprender TS/JS, né?).
- **Ferramenta base:** Eu usei o **Vite** para criar esse projeto. Ele é um empacotador super rápido.
- **Como rodar:** 
  1. Abra seu terminal (Pode ser o PowerShell ou o Git Bash).
  2. Navegue até a pasta: `cd frontend`
  3. Como eu já instalei as dependências, é só rodar: `npm run dev`
  4. Ele vai te dar um link local (algo como `http://localhost:5173`). Clica nele e veja a mágica!

### 2. A pasta `/backend`
Aqui está o servidor, a lógica que vai processar os dados do usuário e cuspir a recomendação do carro.
- **Tecnologia:** Python com FastAPI.
- **Por que isso?** FastAPI é moderno, rápido e maravilhoso para criar APIs. Python é a linguagem perfeita para a lógica de recomendação.
- **Banco de Dados:** **SQLite**. Eu criei um script chamado `init_db.py`. Ele cria um arquivo `database.db` que guarda os carros. É o jeito mais fácil de aprender SQL (SELECT, INSERT, UPDATE, DELETE) sem precisar instalar um servidor de banco de dados gigantesco.
- **Como rodar:**
  1. No PowerShell, navegue até a pasta: `cd backend`
  2. Ative o ambiente virtual que eu criei para as dependências não zoarem seu PC: `.\.venv\Scripts\activate` (no Linux/Bash seria `source .venv/bin/activate`).
  3. Rode a API: `uvicorn main:app --reload`
  4. Acesse no navegador: `http://127.0.0.1:8000/docs` (o FastAPI já cria uma página linda documentando a sua API!).

---

## 🗺️ O Seu Mapa da Mina (O que você precisa aprender/fazer)

Agora é com você. O projeto tem a base, mas não faz o que prometemos ainda. Aqui vai o seu "Roadmap" de estudos e implementação:

### Passo 1: Dominar o Terminal e o Git (Básico)
- **Pesquisa:** Como navegar em pastas usando `cd`, listar arquivos com `ls` ou `dir` no PowerShell.
- **Pesquisa Git:** Como salvar seu código. Estude `git add .`, `git commit -m "mensagem"` e `git push`. (Vou deixar esse projeto já num repositório seu no Github para você ir mandando suas atualizações).

### Passo 2: Entendendo o Banco de Dados (SQL)
- Abra o arquivo `backend/init_db.py`. Veja como eu criei a tabela `cars` usando comandos SQL (`CREATE TABLE`, `INSERT INTO`).
- **Sua Missão:** Popule esse banco de dados! Pesquise dados de carros. Você pode usar a [Tabela FIPE](https://veiculos.fipe.org.br/) ou procurar datasets no [Kaggle](https://www.kaggle.com/) sobre carros (procure por "cars dataset" ou "car prices").
- **Dica:** Adicione mais colunas! Talvez `manutencao_cara` (Booleano) ou `categoria` (Hatch, SUV, Sedan).

### Passo 3: Criar o Algoritmo de Recomendação (Python)
- No `backend/main.py`, eu fiz um endpoint `/cars` que só lista todos os carros do banco.
- **Sua Missão:** Você precisa criar uma função matemática ou baseada em regras (if/else para começar) que receba: a Renda do usuário e a Personalidade dele.
- **Exemplo de Lógica:** Se a renda for menor que R$ 3.000, filtre o banco de dados (usando SQL `WHERE price < X`) trazendo apenas carros de manutenção barata (como um Uno ou Celta). Se a personalidade for "aventureira", dê pontos extras para a categoria SUV/Jeep. Retorne o carro com maior pontuação!

### Passo 4: O Formulário no Frontend (React/TS)
- No Frontend, você vai apagar a página padrão do Vite (dentro de `frontend/src/App.tsx`).
- **Sua Missão:** Crie um formulário! Pergunte o nome do usuário, a renda (input de número) e perguntas de múltipla escolha sobre a personalidade ("Você prefere conforto ou adrenalina?").
- Estude o hook `useState` do React para guardar essas respostas no seu código.

### Passo 5: Juntando tudo (Integração)
- Quando o usuário clicar em "Descobrir meu Carro!", seu Frontend (TS) deve fazer uma requisição HTTP (`fetch` ou `axios`) enviando os dados para o seu Backend (Python).
- O Backend roda o seu algoritmo e devolve um JSON com o carro recomendado.
- O Frontend recebe esse JSON e mostra na tela uma foto linda do carro, o preço e o porquê dele ter sido escolhido!

---

## 📚 Materiais de Apoio Recomendados para você pesquisar
- Para React e TypeScript: Documentação oficial do React (react.dev) é ouro.
- Para Python e FastAPI: O site do FastAPI (fastapi.tiangolo.com) tem um dos melhores tutoriais da internet.
- Para SQL: w3schools.com/sql
- Sobre Algoritmos de recomendação: Pesquise por "Sistemas de recomendação baseados em conhecimento" (Knowledge-based recommender systems). Não precisa usar Inteligência Artificial por enquanto, matemática simples e `IFs` resolvem muito bem para começar!

Mãos à obra, Tarnished_Lucy! O mundo da programação é quebrar a cabeça até funcionar. Eu acredito em você, agora vai lá e faz esse app de carros rodar! 🏎️💨
