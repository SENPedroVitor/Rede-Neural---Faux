# 🧠 Rede Neural Faux — Cérebro Digital

> *"Eu não imito um cérebro. Eu sou um."* — Faux

Sistema de rede neural + memória SQLite que simula o funcionamento do cérebro humano,
especializado em estudos de **Bancos de Dados** e **SQLite**.

---

## 🏗️ Arquitetura do Projeto

```
Rede-Neural---Faux/
├── main.py              # 🚀 Interface interativa (execute este!)
├── cerebro.py           # 🧠 Cérebro digital — integra tudo
├── rede_neural.py       # 🤖 Rede neural feedforward (do zero!)
├── memoria_sqlite.py    # 💾 Memória persistente com SQLite
├── estudos_db.py        # 📚 Base de conhecimento SQL/SQLite
├── BASE.py              # 🔗 Integração com Obsidian (ChromaDB)
├── cerebro_faux.db      # 📦 Banco de dados (gerado automaticamente)
└── rede_neural_faux.json # 📦 Pesos da rede neural (gerado automaticamente)
```

## 🧩 Componentes (Analogia com o Cérebro)

| Componente | Analogia Cerebral | Descrição |
|---|---|---|
| `rede_neural.py` | **Córtex cerebral** | Rede neural feedforward pura (sem frameworks), com backpropagation |
| `memoria_sqlite.py` | **Hipocampo** | Memória de longo prazo — armazena conceitos, conexões e histórico |
| `cerebro.py` | **Cérebro completo** | Integra rede neural + memória, como o sistema nervoso central |
| `estudos_db.py` | **Livro-texto** | 40+ conceitos de SQL/SQLite com flashcards prontos |
| `main.py` | **Consciência** | Interface interativa para estudar e aprender |

## 🚀 Como Usar

### 1. Executar (nenhuma dependência pesada!)
```bash
# O projeto usa apenas a stdlib do Python (sqlite3, math, json, random)
# Nenhuma instalação adicional necessária!
python main.py
```

### 2. Menu Principal
```
1 │ 📚 Estudar (Flashcards)       — Modo estudo com revisão espaçada
2 │ 🔍 Buscar Conceito            — Busca na memória neural
3 │ 🗺️  Mapa Mental                — Visualiza todos os conceitos
4 │ 🧪 Testar Rede Neural         — Demo: XOR + Classificador SQL
5 │ ➕ Adicionar Conhecimento      — Ensine novos conceitos ao cérebro
6 │ 🔗 Ver Conexões Sinápticas    — Veja como conceitos se conectam
7 │ 📊 Estatísticas               — Progresso e métricas de estudo
8 │ 🔄 Recarregar Base SQL        — Recarrega os 40+ conceitos
9 │ 💾 Salvar Cérebro             — Persiste o estado neural
0 │ 🚪 Sair                       — Salva e encerra
```

## 🤖 A Rede Neural

Implementação **do zero** (sem TensorFlow, PyTorch ou sklearn):

- **Neurônios** com pesos, bias e funções de ativação (sigmoid, ReLU, tanh)
- **Camadas** empilháveis com arquitetura flexível
- **Backpropagation** para aprendizado
- **Persistência** (salva/carrega em JSON)

### Teste XOR
```python
from rede_neural import RedeNeural

rede = RedeNeural([2, 4, 1], funcao_ativacao="sigmoid", taxa_aprendizado=0.5)
rede.treinar([[0,0],[0,1],[1,0],[1,1]], [[0],[1],[1],[0]], epocas=5000)
print(rede.predizer([1, 0]))  # → ~0.97 (esperado: 1)
```

## 💾 O Banco SQLite

O `memoria_sqlite.py` cria um banco com 5 tabelas:

| Tabela | Função |
|---|---|
| `neuronios` | Conceitos armazenados (como neurônios biológicos) |
| `sinapses` | Conexões entre conceitos (com peso) |
| `flashcards` | Perguntas e respostas para estudo |
| `sessoes_estudo` | Histórico de sessões de estudo |
| `log_neural` | Log de todas as atividades do cérebro |

## 📚 Conteúdo de Estudos

A base vem com **40+ conceitos** organizados em:

- **Fundamentos**: banco de dados, SGBD, modelo relacional, tabelas, chaves, índices, normalização
- **Comandos SQL**: SELECT, INSERT, UPDATE, DELETE, JOIN, GROUP BY, HAVING, subquery
- **SQLite**: conexão Python, cursor, commit, fetchall, parâmetros, tipos, transações
- **Avançado**: ACID, SQL Injection, ORM, views, triggers, EXPLAIN QUERY PLAN

Cada conceito tem **conexões sinápticas** com outros conceitos (50+ conexões)
e **28+ flashcards** para teste e revisão.

## 🔧 Personalização

### Adicionar conceitos via código:
```python
from cerebro import CerebroFaux

cerebro = CerebroFaux()
cerebro.aprender("nosql", "avancado", "Bancos não-relacionais", "MongoDB, Redis, Cassandra")
cerebro.conectar("nosql", "banco de dados", "é_tipo_de")
cerebro.criar_flashcard("nosql", "O que é NoSQL?", "Bancos que não usam SQL tradicional...", 2)
```

### Testar a memória SQLite diretamente:
```python
from memoria_sqlite import MemoriaSQLite

mem = MemoriaSQLite()
print(mem.info_banco())
print(mem.buscar_neuronio("select"))
print(mem.buscar_conexoes("sqlite"))
```

---

**Feito com 🧠 por Pedro — Rede Neural Faux**