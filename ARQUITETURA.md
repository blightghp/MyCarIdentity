# Arquitetura & Roadmap — MyCarIdentity

**Autor:** Fernando  
**Última atualização:** Julho/2026  
**Status:** Em construção 🚧

---

## Sumário

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Arquitetura do Sistema](#2-arquitetura-do-sistema)
3. [Estrutura de Pastas](#3-estrutura-de-pastas)
4. [Stack Tecnológica (e por que cada escolha)](#4-stack-tecnológica)
5. [Modelo de Dados (o coração do negócio)](#5-modelo-de-dados)
6. [O Motor de Recomendação](#6-o-motor-de-recomendação)
7. [Roadmap de Desenvolvimento (Etapas)](#7-roadmap-de-desenvolvimento)
8. [Fontes de Dados e Pesquisas Necessárias](#8-fontes-de-dados)
9. [Padrões de Código e Estilo](#9-padrões-de-código)
10. [Glossário Técnico para Iniciantes](#10-glossário-técnico)

---

## 1. Visão Geral do Projeto

O **MyCarIdentity** é um app web que responde duas perguntas que todo mundo que gosta de carro já fez:

> *"Qual carro reflete quem eu sou?"*

e a mais importante pra maioria dos brasileiros:

> *"Com o que eu ganho, qual carro combina comigo de verdade?"*

A ideia é simples: o usuário preenche um questionário com seus dados financeiros, estilo de vida e preferências pessoais. O sistema cruza tudo isso com um banco de dados de carros do mercado brasileiro e devolve uma lista ranqueada de recomendações — cada uma com justificativa e simulação financeira.

Não tem nada de mágica aqui: é matemática, peso, filtro e lógica de negócio. O nome bonito pra isso no mercado é **sistema de recomendação baseado em conhecimento** (knowledge-based recommender). A diferença do que você vê na Netflix (que é collaborative filtering) é que aqui a gente não precisa de milhares de usuários pra funcionar — a lógica é determinística e explícita.

---

## 2. Arquitetura do Sistema

O projeto segue a arquitetura clássica **cliente-servidor** (two-tier com API REST no meio):

```
┌──────────────────────────────────────────────────────────────────┐
│                        NAVEGADOR DO USUÁRIO                      │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  FRONTEND (React + TypeScript)                             │  │
│  │  - Formulário de Quiz (multi-step)                         │  │
│  │  - Painel de Resultados                                    │  │
│  │  - Catálogo de Carros                                      │  │
│  │  - Componentes visuais (cards, gráficos)                   │  │
│  └──────────────────────┬─────────────────────────────────────┘  │
│                         │ HTTP (fetch / axios)                    │
│                         │ JSON                                    │
└─────────────────────────┼────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│  BACKEND (Python + FastAPI)                                      │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │
│  │  Rotas/API   │ │  Recommender │ │  Modelos (Pydantic)      │ │
│  │  (routes.py) │ │  Engine      │ │  (models.py)             │ │
│  │              │ │  (recomm.py) │ │                          │ │
│  └──────┬───────┘ └──────┬───────┘ └──────────────────────────┘ │
│         │                │                                       │
│         └────────┬───────┘                                       │
│                  │                                                │
│                  ▼                                                │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  BANCO DE DADOS (SQLite)                                   │  │
│  │  - Tabela: cars (catálogo completo)                        │  │
│  │  - Tabela: user_profiles (histórico, futuro)               │  │
│  │  - Tabela: recommendations_log (auditoria, futuro)         │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

### Por que essa arquitetura?

- **Separação de responsabilidades:** o frontend não sabe nada de SQL, e o backend não sabe nada de CSS. Cada um cuida do seu.
- **API REST:** é o padrão que 90% das empresas usam. Aprender isso aqui vale pra qualquer vaga de emprego.
- **SQLite:** zero configuração, arquivo local, perfeito pra aprender SQL sem instalar PostgreSQL/MySQL. Quando o projeto crescer, a migração é quase transparente.

---

## 3. Estrutura de Pastas

```
MyCarIdentity/
│
├── README.md                    # Descrição geral do projeto (GitHub)
├── README_FER.md                # Guia inicial que o Fer escreveu pro Lucy
├── ARQUITETURA.md               # << ESTE DOCUMENTO >>
├── .gitignore
│
├── backend/
│   ├── .venv/                   # Ambiente virtual Python (NÃO commitar)
│   ├── main.py                  # Ponto de entrada do servidor FastAPI
│   ├── routes.py                # Rotas/endpoints da API
│   ├── models.py                # Modelos de dados (Pydantic)
│   ├── database.py              # Conexão e setup do SQLite
│   ├── recommender.py           # Motor de recomendação (a lógica pesada)
│   ├── init_db.py               # Script pra popular o banco com dados iniciais
│   ├── requirements.txt         # Dependências Python
│   └── database.db              # Arquivo do SQLite (NÃO commitar, gerado pelo init_db)
│
└── frontend/
    ├── node_modules/            # Dependências JS (NÃO commitar)
    ├── public/                  # Assets estáticos
    ├── src/
    │   ├── main.tsx             # Entry point do React
    │   ├── App.tsx              # Componente raiz
    │   ├── App.css              # Estilos globais do App
    │   ├── index.css            # Reset e base CSS
    │   ├── types/
    │   │   └── index.ts         # Interfaces TypeScript (espelha os models do backend)
    │   ├── services/
    │   │   └── api.ts           # Módulo de comunicação com o backend
    │   ├── components/
    │   │   ├── QuizForm.tsx     # Formulário multi-step do quiz de personalidade
    │   │   ├── CarCard.tsx      # Card visual de exibição de um carro
    │   │   └── ResultPanel.tsx  # Painel de resultados/recomendações
    │   └── styles/
    │       └── variables.css    # Variáveis CSS (cores, fontes, espaçamentos)
    ├── package.json
    ├── tsconfig.json
    └── vite.config.ts
```

---

## 4. Stack Tecnológica

| Camada    | Tecnologia          | Versão    | Por quê?                                                       |
|-----------|---------------------|-----------|----------------------------------------------------------------|
| Frontend  | React               | 19.x      | Biblioteca UI dominante no mercado, componentização, hooks     |
| Frontend  | TypeScript          | 6.x       | Tipagem estática = menos bug, autocompletar melhor, disciplina |
| Frontend  | Vite                | 8.x       | Build tool rápido, HMR instantâneo, config mínima             |
| Backend   | Python              | 3.14      | Versatilidade, ótimo pra lógica de dados e algoritmos          |
| Backend   | FastAPI             | 0.139     | Moderno, tipado, docs automáticas (Swagger), async-ready       |
| Backend   | Pydantic            | 2.x       | Validação de dados integrada com FastAPI, type hints nativo    |
| Backend   | Uvicorn             | 0.51      | Servidor ASGI leve e rápido                                    |
| Banco     | SQLite              | (embutido)| Zero setup, aprende SQL puro, arquivo portátil                 |
| Controle  | Git + GitHub        | —         | Versionamento, colaboração, portfolio                          |
| Terminal  | PowerShell / Bash   | —         | Automação, scripts, fluência no terminal                       |

---

## 5. Modelo de Dados

### 5.1 Tabela `cars` (SQLite)

Essa é a tabela central. Cada registro é um carro do mercado brasileiro.

| Coluna                  | Tipo     | Descrição                                              |
|-------------------------|----------|--------------------------------------------------------|
| `id`                    | INTEGER  | PK, auto-increment                                    |
| `modelo`                | TEXT     | Nome do modelo (ex: "HB20", "Civic")                  |
| `marca`                 | TEXT     | Fabricante (ex: "Hyundai", "Honda")                    |
| `ano_fabricacao`        | INTEGER  | Ano de fabricação                                      |
| `ano_modelo`            | INTEGER  | Ano do modelo                                          |
| `preco_fipe`            | REAL     | Preço pela tabela FIPE (R$)                            |
| `preco_mercado`         | REAL     | Preço médio no mercado (R$)                            |
| `categoria`             | TEXT     | hatch, sedan, suv, pickup, esportivo, luxo             |
| `combustivel`           | TEXT     | flex, gasolina, diesel, eletrico, hibrido              |
| `cambio`                | TEXT     | manual, automatico, cvt, automatizado                  |
| `manutencao_custo_mensal`| REAL    | Custo médio mensal de manutenção (R$)                  |
| `seguro_medio_anual`    | REAL     | Valor médio do seguro por ano (R$)                     |
| `consumo_cidade`        | REAL     | km/l na cidade                                         |
| `consumo_estrada`       | REAL     | km/l na estrada                                        |
| `nota_seguranca`        | INTEGER  | 1 a 5 (nota subjetiva / Latin NCAP)                   |
| `nota_conforto`         | INTEGER  | 1 a 5                                                  |
| `nota_desempenho`       | INTEGER  | 1 a 5                                                  |
| `nota_custo_beneficio`  | INTEGER  | 1 a 5                                                  |
| `imagem_url`            | TEXT     | URL de uma imagem do carro (pode ser placeholder)      |
| `descricao`             | TEXT     | Texto descritivo livre sobre o carro                   |

### 5.2 Perfil do Usuário (input do quiz)

Esses dados vêm do formulário no frontend e são enviados via POST:

| Campo              | Tipo       | Descrição                                                    |
|--------------------|------------|--------------------------------------------------------------|
| `nome`             | string     | Nome do usuário                                              |
| `renda_mensal`     | float      | Renda mensal líquida (R$)                                    |
| `valor_entrada`    | float      | Quanto pode dar de entrada (R$)                              |
| `parcelas_max`     | int        | Máximo de parcelas que aceita (12, 24, 36, 48, 60)           |
| `personalidade`    | string     | aventureiro, conservador, esportivo, economico, status       |
| `prioridades`      | string[]   | Lista ordenada: seguranca, economia, conforto, desempenho, estetica |
| `uso_principal`    | string     | cidade, estrada, misto                                       |

### 5.3 Resposta de Recomendação (output da API)

| Campo                       | Tipo   | Descrição                                          |
|-----------------------------|--------|----------------------------------------------------|
| `car`                       | Car    | Objeto completo do carro recomendado               |
| `score`                     | float  | Pontuação calculada (0.0 a 100.0)                  |
| `justificativa`             | string | Texto explicando por que esse carro combina        |
| `parcela_estimada`          | float  | Valor estimado da parcela mensal (R$)              |
| `comprometimento_renda_pct` | float  | % da renda que seria comprometida                  |

---

## 6. O Motor de Recomendação

### 6.1 Visão geral do algoritmo

O motor funciona em **3 fases sequenciais**:

```
FASE 1: FILTRO          FASE 2: PONTUAÇÃO         FASE 3: RANKING
───────────────         ─────────────────         ────────────────
Elimina carros    →     Calcula score de    →     Ordena por score
que o usuário           cada carro restante       e monta o top N
não pode pagar          com base nas               com justificativas
                        preferências
```

### 6.2 Fase 1 — Filtro por capacidade financeira

Aqui é pura matemática financeira básica. A ideia:

1. Calcula o **valor máximo financiável**: `valor_entrada + (parcelas_max * parcela_max_aceitavel)`
2. A `parcela_max_aceitavel` é `renda_mensal * 0.30` (regra clássica dos 30% de comprometimento)
3. Filtra fora qualquer carro com `preco_mercado > valor_maximo`
4. Também filtra carros cuja manutenção mensal + parcela ultrapassem 40% da renda

### 6.3 Fase 2 — Pontuação por personalidade e prioridades

Cada carro recebe uma pontuação de 0 a 100 baseada em **pesos**:

```
Score = (P1 * nota_criterio_1) + (P2 * nota_criterio_2) + ... + bonus_personalidade
```

Os pesos (P1, P2...) são definidos pelas **prioridades** do usuário. Se ele marcou "segurança" como prioridade #1, a `nota_seguranca` do carro ganha peso maior.

Distribuição de pesos sugerida (somam 1.0):

| Posição da prioridade | Peso  |
|------------------------|-------|
| 1ª prioridade          | 0.35  |
| 2ª prioridade          | 0.25  |
| 3ª prioridade          | 0.20  |
| 4ª prioridade          | 0.12  |
| 5ª prioridade          | 0.08  |

Mapeamento prioridade → nota do carro:

| Prioridade   | Campo usado              |
|--------------|--------------------------|
| seguranca    | nota_seguranca           |
| economia     | nota_custo_beneficio     |
| conforto     | nota_conforto            |
| desempenho   | nota_desempenho          |
| estetica     | (nota_conforto + nota_desempenho) / 2  |

O **bonus de personalidade** é um multiplicador de 1.0x a 1.3x que aumenta o score quando a categoria do carro "casa" com a personalidade do usuário:

| Personalidade | Categorias que ganham bônus      | Multiplicador |
|---------------|----------------------------------|---------------|
| aventureiro   | suv, pickup                      | 1.25x         |
| conservador   | sedan, hatch                     | 1.15x         |
| esportivo     | esportivo, sedan (turbo-ish)     | 1.30x         |
| economico     | hatch, sedan (compacto)          | 1.20x         |
| status        | luxo, suv (premium)              | 1.25x         |

### 6.4 Fase 3 — Ranking e justificativa

1. Ordena os carros por score decrescente
2. Pega os top N (padrão: 5)
3. Para cada um, gera uma `justificativa` automática baseada nos critérios que mais contribuíram para o score
4. Calcula a `parcela_estimada` e o `comprometimento_renda_pct`

### 6.5 Algoritmos e estruturas de dados envolvidos

Para o Lucy estudar e entender o que está por trás:

- **Ordenação:** `sorted()` do Python com `key=lambda` — é um Timsort (merge sort + insertion sort híbrido, O(n log n))
- **Filtragem:** List comprehension com predicado — O(n) linear
- **Pontuação:** Soma ponderada (weighted sum) — conceito fundamental de álgebra linear
- **Simulação financeira:** Juros compostos simplificado (Price) — `PMT = PV * [i(1+i)^n] / [(1+i)^n - 1]`

Pesquisas sugeridas: *"weighted scoring model"*, *"knowledge-based recommender system"*, *"tabela Price financiamento"*.

---

## 7. Roadmap de Desenvolvimento

O desenvolvimento deve seguir **exatamente** essa ordem. Cada etapa depende da anterior.

### ETAPA 1 — Fundação do Backend (banco + modelos)
**Estimativa:** 1-2 sprints  
**Branch sugerida:** `feat/backend-foundation`

**O que fazer:**
1. Revisar e expandir o `database.py` — garantir que o schema da tabela `cars` bate com o modelo de dados da Seção 5
2. Expandir o `init_db.py` — popular com pelo menos 25 carros reais do mercado brasileiro, com preços atualizados da FIPE
3. Validar os `models.py` (Pydantic) — garantir que os tipos estão corretos e a validação funciona
4. Testar tudo no terminal: `python init_db.py`, depois `python -c "from database import get_connection; ..."`

**Critério de "pronto":**
- [ ] Banco criado com 25+ carros
- [ ] Models validando input corretamente
- [ ] Consegue fazer SELECT no terminal e ver os dados

---

### ETAPA 2 — API REST (rotas e endpoints)
**Estimativa:** 1-2 sprints  
**Branch sugerida:** `feat/api-routes`

**O que fazer:**
1. Implementar todas as rotas do `routes.py`
2. Integrar as rotas no `main.py` com `app.include_router()`
3. Configurar CORS no FastAPI (senão o frontend não consegue chamar a API)
4. Testar cada endpoint pelo Swagger UI (`/docs`)

**Critério de "pronto":**
- [ ] GET /api/carros retorna lista de carros em JSON
- [ ] GET /api/carros/1 retorna um carro específico
- [ ] POST /api/recomendar aceita um body JSON e retorna recomendações
- [ ] Swagger UI funcional em localhost:8000/docs

---

### ETAPA 3 — Motor de Recomendação
**Estimativa:** 2-3 sprints  
**Branch sugerida:** `feat/recommender-engine`

**O que fazer:**
1. Implementar o `recommender.py` seguindo a lógica da Seção 6
2. Começar com uma versão simples (filtro por preço + if/else de personalidade)
3. Evoluir para a versão com pesos e scoring
4. Adicionar a geração de justificativas textuais
5. Testar com perfis fictícios variados (renda alta/baixa, personalidades diferentes)

**Critério de "pronto":**
- [ ] Motor retorna top 5 carros para um perfil de teste
- [ ] Justificativas fazem sentido textualmente
- [ ] Parcela estimada está calculada corretamente
- [ ] Carros fora do orçamento NÃO aparecem

---

### ETAPA 4 — Frontend: Estrutura e Quiz
**Estimativa:** 2-3 sprints  
**Branch sugerida:** `feat/frontend-quiz`

**O que fazer:**
1. Limpar o App.tsx (remover boilerplate do Vite)
2. Implementar o `QuizForm.tsx` com formulário multi-step
3. Implementar o `api.ts` para comunicação com o backend
4. Criar as variáveis CSS globais (`variables.css`)
5. Testar o fluxo: preencher quiz → ver request no Network tab do navegador

**Critério de "pronto":**
- [ ] Formulário de quiz funcionando com todos os campos
- [ ] Dados sendo enviados corretamente ao backend via POST
- [ ] Console mostra a resposta da API sem erros

---

### ETAPA 5 — Frontend: Resultados e Visual
**Estimativa:** 2-3 sprints  
**Branch sugerida:** `feat/frontend-results`

**O que fazer:**
1. Implementar o `CarCard.tsx` com design caprichado
2. Implementar o `ResultPanel.tsx` para exibir as recomendações
3. Adicionar indicador visual de comprometimento de renda (verde/amarelo/vermelho)
4. Estilizar tudo — dark theme, gradientes, transições suaves, hover effects
5. Responsividade básica (mobile-first)

**Critério de "pronto":**
- [ ] Resultado renderiza os carros recomendados visualmente
- [ ] Score e justificativa aparecem para cada carro
- [ ] Indicador de comprometimento de renda funciona
- [ ] Layout decente em desktop e mobile

---

### ETAPA 6 — Polimento e Features Extras
**Estimativa:** 2+ sprints  
**Branch sugerida:** `feat/polish`

**O que fazer:**
1. Tratamento de erros (loading states, mensagens amigáveis)
2. Animações de transição entre steps do quiz
3. Página de catálogo (listar todos os carros com filtros)
4. Comparação lado a lado de 2-3 carros
5. Salvar resultado do quiz (localStorage ou banco)
6. Melhorar os dados: puxar preços atualizados da FIPE

**Ideias futuras (muito mais pra frente):**
- Integração com API da FIPE (se existir pública)
- Login/cadastro com histórico de quizzes
- Machine Learning: treinar um modelo com dados reais de satisfação
- Deploy em produção (Vercel pro front, Railway/Render pro back)

---

## 8. Fontes de Dados e Pesquisas

### Bancos de dados de carros (para popular o SQLite)

| Fonte                           | URL                                     | O que tem                            |
|---------------------------------|------------------------------------------|------------------------------------|
| Tabela FIPE                     | https://veiculos.fipe.org.br/            | Preços de referência, todos os modelos |
| FIPE API (não-oficial)          | https://brasilapi.com.br/docs#tag/FIPE   | API REST gratuita com dados FIPE    |
| Kaggle - Brazilian Cars         | Procurar "brazil cars dataset"           | Datasets prontos em CSV             |
| Webmotors / iCarros             | Scraping (estudo)                        | Preços de mercado reais             |
| Latin NCAP                      | https://www.latinncap.com/               | Notas de segurança                  |
| Quatro Rodas (revista)          | Avaliações de carros                     | Notas de conforto/desempenho        |

### Pesquisas técnicas recomendadas

| Tema                                        | Por quê                                     |
|---------------------------------------------|---------------------------------------------|
| "knowledge-based recommender system"        | Entender o tipo de algoritmo que estamos usando |
| "weighted scoring model decision making"    | A matemática por trás do rankeamento        |
| "tabela Price financiamento cálculo"        | Como bancos calculam parcela de carro       |
| "REST API best practices"                   | Padrões de design de API                    |
| "React useState useEffect tutorial"         | Hooks fundamentais do React                 |
| "TypeScript interfaces vs types"            | Tipagem no frontend                         |
| "SQLite tutorial Python"                    | Operações CRUD com sqlite3                  |
| "CSS custom properties design system"       | Como montar uma paleta de cores profissional |
| "git branching strategy"                    | Como organizar branches (git flow simplificado) |

---

## 9. Padrões de Código e Estilo

### Python (Backend)
- **Nomes:** `snake_case` para variáveis, funções e arquivos
- **Docstrings:** breves, em português, na primeira linha da função
- **Type hints:** obrigatórios em parâmetros e retornos
- **Comentários:** em português, quando necessário (não comentar o óbvio)
- **Imports:** stdlib primeiro, depois terceiros, depois locais (PEP 8)

### TypeScript/React (Frontend)
- **Nomes:** `camelCase` para variáveis/funções, `PascalCase` para componentes e tipos
- **Interfaces:** prefira `interface` para objetos, `type` para unions/aliases
- **Componentes:** funcionais com hooks (nada de classes)
- **CSS:** vanilla CSS com variáveis (custom properties), arquivos `.css` por componente quando necessário
- **Comentários:** em português, pragmáticos

### Git
- **Commits:** mensagens em português, no imperativo: `"Adiciona endpoint de recomendação"`, `"Corrige cálculo de parcela"`
- **Branches:** `feat/nome-curto`, `fix/nome-curto`, `refactor/nome-curto`
- **Nunca commitar:** `node_modules/`, `.venv/`, `database.db`, `.env`

---

## 10. Glossário Técnico para Iniciantes

| Termo               | O que é                                                                  |
|----------------------|--------------------------------------------------------------------------|
| **API**              | Interface de Programação — o "contrato" entre frontend e backend         |
| **REST**             | Estilo de arquitetura de API usando HTTP (GET, POST, PUT, DELETE)         |
| **Endpoint**         | Uma URL específica da API (ex: `/api/carros`)                            |
| **JSON**             | Formato de dados universal (JavaScript Object Notation)                  |
| **Pydantic**         | Biblioteca Python pra validar dados usando type hints                    |
| **FastAPI**          | Framework Python pra criar APIs REST rapidamente                         |
| **React**            | Biblioteca JS pra construir interfaces com componentes reutilizáveis     |
| **TypeScript**       | JavaScript com tipos — pega erros antes de rodar o código                |
| **Vite**             | Ferramenta que empacota e serve seu frontend com reload instantâneo      |
| **SQLite**           | Banco de dados relacional que roda num arquivo só, sem servidor          |
| **SQL**              | Linguagem pra consultar bancos de dados (SELECT, INSERT, UPDATE, DELETE) |
| **FIPE**             | Fundação Instituto de Pesquisas Econômicas — tabela de preços de veículos|
| **Hooks (React)**    | Funções especiais (useState, useEffect) pra gerenciar estado e efeitos   |
| **CORS**             | Mecanismo de segurança do navegador — precisa configurar no backend      |
| **HMR**              | Hot Module Replacement — atualiza o browser sem dar refresh              |
| **CRUD**             | Create, Read, Update, Delete — as 4 operações básicas de qualquer sistema|
| **Scoring**          | Sistema de pontuação pra rankear resultados                              |
| **PK**               | Primary Key — identificador único de um registro no banco                |

---

> **Nota do Fer:** Esse documento é vivo. Conforme o projeto avança, eu atualizo aqui. Se alguma coisa não fizer sentido, me chama que a gente resolve junto. O importante é entender o *porquê* de cada decisão, não só copiar e colar. Bora! 🏎️
