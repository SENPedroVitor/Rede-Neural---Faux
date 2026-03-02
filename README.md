# Rede Neural Faux -- Cerebro Digital

> *"Eu nao imito um cerebro. Eu sou um."* -- Faux

Sistema de rede neural + memoria SQLite que simula o funcionamento do cerebro humano,
especializado em estudos de **Bancos de Dados** e **SQLite**.

---

## Arquitetura do Projeto

```
Rede-Neural---Faux/
├── main.py              # Interface interativa (execute este!)
├── cerebro.py           # Cerebro digital -- integra tudo
├── rede_neural.py       # Rede neural feedforward (do zero!)
├── memoria_sqlite.py    # Memoria persistente com SQLite
├── estudos_db.py        # Base de conhecimento SQL/SQLite
├── BASE.py              # Integracao com Obsidian (ChromaDB)
├── cerebro_faux.db      # Banco de dados (gerado automaticamente)
└── rede_neural_faux.json # Pesos da rede neural (gerado automaticamente)
```

## Componentes (Analogia com o Cerebro)

| Componente | Analogia Cerebral | Descricao |
|---|---|---|
| `rede_neural.py` | **Cortex cerebral** | Rede neural feedforward pura (sem frameworks), com backpropagation |
| `memoria_sqlite.py` | **Hipocampo** | Memoria de longo prazo -- armazena conceitos, conexoes e historico |
| `cerebro.py` | **Cerebro completo** | Integra rede neural + memoria, como o sistema nervoso central |
| `estudos_db.py` | **Livro-texto** | 40+ conceitos de SQL/SQLite com flashcards prontos |
| `main.py` | **Consciencia** | Interface interativa para estudar e aprender |

## Como Usar

### 1. Executar (nenhuma dependencia pesada!)
```bash
# O projeto usa apenas a stdlib do Python (sqlite3, math, json, random)
# Nenhuma instalacao adicional necessaria!
python main.py
```

### 2. Menu Principal
```
1 | Estudar (Flashcards)       -- Modo estudo com revisao espacada
2 | Buscar Conceito            -- Busca na memoria neural
3 | Mapa Mental                -- Visualiza todos os conceitos
4 | Testar Rede Neural         -- Demo: XOR + Classificador SQL
5 | Adicionar Conhecimento     -- Ensine novos conceitos ao cerebro
6 | Ver Conexoes Sinapticas    -- Veja como conceitos se conectam
7 | Estatisticas               -- Progresso e metricas de estudo
8 | Recarregar Base SQL        -- Recarrega os 40+ conceitos
9 | Salvar Cerebro             -- Persiste o estado neural
0 | Sair                       -- Salva e encerra
```

## A Rede Neural

Implementacao **do zero** (sem TensorFlow, PyTorch ou sklearn):

- **Neuronios** com pesos, bias e funcoes de ativacao (sigmoid, ReLU, tanh)
- **Camadas** empilhaveis com arquitetura flexivel
- **Backpropagation** para aprendizado
- **Persistencia** (salva/carrega em JSON)

### Teste XOR
```python
from rede_neural import RedeNeural

rede = RedeNeural([2, 4, 1], funcao_ativacao="sigmoid", taxa_aprendizado=0.5)
rede.treinar([[0,0],[0,1],[1,0],[1,1]], [[0],[1],[1],[0]], epocas=5000)
print(rede.predizer([1, 0]))  # -> ~0.97 (esperado: 1)
```

## O Banco SQLite

O `memoria_sqlite.py` cria um banco com 5 tabelas:

| Tabela | Funcao |
|---|---|
| `neuronios` | Conceitos armazenados (como neuronios biologicos) |
| `sinapses` | Conexoes entre conceitos (com peso) |
| `flashcards` | Perguntas e respostas para estudo |
| `sessoes_estudo` | Historico de sessoes de estudo |
| `log_neural` | Log de todas as atividades do cerebro |

## Conteudo de Estudos

A base vem com **40+ conceitos** organizados em:

- **Fundamentos**: banco de dados, SGBD, modelo relacional, tabelas, chaves, indices, normalizacao
- **Comandos SQL**: SELECT, INSERT, UPDATE, DELETE, JOIN, GROUP BY, HAVING, subquery
- **SQLite**: conexao Python, cursor, commit, fetchall, parametros, tipos, transacoes
- **Avancado**: ACID, SQL Injection, ORM, views, triggers, EXPLAIN QUERY PLAN

Cada conceito tem **conexoes sinapticas** com outros conceitos (50+ conexoes)
e **28+ flashcards** para teste e revisao.

## Personalizacao

### Adicionar conceitos via codigo:
```python
from cerebro import CerebroFaux

cerebro = CerebroFaux()
cerebro.aprender("nosql", "avancado", "Bancos nao-relacionais", "MongoDB, Redis, Cassandra")
cerebro.conectar("nosql", "banco de dados", "e_tipo_de")
cerebro.criar_flashcard("nosql", "O que e NoSQL?", "Bancos que nao usam SQL tradicional...", 2)
```

### Testar a memoria SQLite diretamente:
```python
from memoria_sqlite import MemoriaSQLite

mem = MemoriaSQLite()
print(mem.info_banco())
print(mem.buscar_neuronio("select"))
print(mem.buscar_conexoes("sqlite"))
```

---

**Feito por Pedro -- Rede Neural Faux**