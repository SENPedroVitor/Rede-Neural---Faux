"""
estudos_db.py — Base de Conhecimento sobre Bancos de Dados e SQLite
===================================================================
Popula o cérebro com conhecimento estruturado sobre DB e SQLite.
Inclui conceitos, conexões sinápticas e flashcards para estudo.
"""

from cerebro import CerebroFaux


def carregar_conhecimento_sql(cerebro: CerebroFaux):
    """Carrega o conhecimento fundamental sobre SQL e Bancos de Dados."""

    print("\nCarregando base de conhecimento: SQL & Bancos de Dados...")
    print("=" * 60)

    # ════════════════════════════════════════════════════════════════
    # 1. CONCEITOS FUNDAMENTAIS DE BANCO DE DADOS
    # ════════════════════════════════════════════════════════════════

    conceitos_fundamentos = [
        {
            "conceito": "banco de dados",
            "categoria": "fundamentos",
            "descricao": "Coleção organizada de dados estruturados, armazenados eletronicamente",
            "exemplos": "MySQL, PostgreSQL, SQLite, MongoDB, Oracle"
        },
        {
            "conceito": "sgbd",
            "categoria": "fundamentos",
            "descricao": "Sistema Gerenciador de Banco de Dados — software que gerencia o acesso aos dados",
            "exemplos": "MySQL Server, PostgreSQL, SQLite3, SQL Server"
        },
        {
            "conceito": "modelo relacional",
            "categoria": "fundamentos",
            "descricao": "Modelo que organiza dados em tabelas (relações) com linhas e colunas",
            "exemplos": "Tabela Alunos com colunas: id, nome, idade, curso"
        },
        {
            "conceito": "tabela",
            "categoria": "fundamentos",
            "descricao": "Estrutura que armazena dados em linhas (registros) e colunas (campos)",
            "exemplos": "CREATE TABLE alunos (id INTEGER, nome TEXT, idade INTEGER)"
        },
        {
            "conceito": "registro",
            "categoria": "fundamentos",
            "descricao": "Uma linha em uma tabela, representando uma instância de dado",
            "exemplos": "INSERT INTO alunos VALUES (1, 'Pedro', 20)"
        },
        {
            "conceito": "campo",
            "categoria": "fundamentos",
            "descricao": "Uma coluna em uma tabela, define o tipo de dado armazenado",
            "exemplos": "nome TEXT, idade INTEGER, salario REAL"
        },
        {
            "conceito": "chave primária",
            "categoria": "fundamentos",
            "descricao": "Campo que identifica unicamente cada registro na tabela (PRIMARY KEY)",
            "exemplos": "id INTEGER PRIMARY KEY AUTOINCREMENT"
        },
        {
            "conceito": "chave estrangeira",
            "categoria": "fundamentos",
            "descricao": "Campo que referencia a chave primária de outra tabela (FOREIGN KEY)",
            "exemplos": "FOREIGN KEY (curso_id) REFERENCES cursos(id)"
        },
        {
            "conceito": "índice",
            "categoria": "fundamentos",
            "descricao": "Estrutura que acelera buscas no banco, como um índice de livro",
            "exemplos": "CREATE INDEX idx_nome ON alunos(nome)"
        },
        {
            "conceito": "normalização",
            "categoria": "fundamentos",
            "descricao": "Processo de organizar tabelas para reduzir redundância (1FN, 2FN, 3FN)",
            "exemplos": "Separar endereço em tabela própria em vez de repetir em cada registro"
        },
    ]

    # ════════════════════════════════════════════════════════════════
    # 2. COMANDOS SQL
    # ════════════════════════════════════════════════════════════════

    conceitos_sql = [
        {
            "conceito": "select",
            "categoria": "sql_comandos",
            "descricao": "Comando para consultar/buscar dados no banco",
            "exemplos": "SELECT nome, idade FROM alunos WHERE idade > 18"
        },
        {
            "conceito": "insert",
            "categoria": "sql_comandos",
            "descricao": "Comando para inserir novos registros em uma tabela",
            "exemplos": "INSERT INTO alunos (nome, idade) VALUES ('Pedro', 20)"
        },
        {
            "conceito": "update",
            "categoria": "sql_comandos",
            "descricao": "Comando para atualizar registros existentes",
            "exemplos": "UPDATE alunos SET idade = 21 WHERE nome = 'Pedro'"
        },
        {
            "conceito": "delete",
            "categoria": "sql_comandos",
            "descricao": "Comando para remover registros de uma tabela",
            "exemplos": "DELETE FROM alunos WHERE id = 5"
        },
        {
            "conceito": "create table",
            "categoria": "sql_comandos",
            "descricao": "Comando DDL para criar uma nova tabela no banco",
            "exemplos": "CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco REAL)"
        },
        {
            "conceito": "alter table",
            "categoria": "sql_comandos",
            "descricao": "Comando DDL para modificar a estrutura de uma tabela existente",
            "exemplos": "ALTER TABLE alunos ADD COLUMN email TEXT"
        },
        {
            "conceito": "drop table",
            "categoria": "sql_comandos",
            "descricao": "Comando DDL para excluir uma tabela e todos seus dados",
            "exemplos": "DROP TABLE IF EXISTS alunos_antigos"
        },
        {
            "conceito": "where",
            "categoria": "sql_comandos",
            "descricao": "Cláusula de filtro — seleciona apenas registros que atendem a condição",
            "exemplos": "SELECT * FROM alunos WHERE idade >= 18 AND curso = 'TI'"
        },
        {
            "conceito": "join",
            "categoria": "sql_comandos",
            "descricao": "Combina registros de duas ou mais tabelas baseado em relação entre elas",
            "exemplos": "SELECT a.nome, c.nome_curso FROM alunos a JOIN cursos c ON a.curso_id = c.id"
        },
        {
            "conceito": "group by",
            "categoria": "sql_comandos",
            "descricao": "Agrupa registros com valores iguais para usar funções de agregação",
            "exemplos": "SELECT curso, COUNT(*) FROM alunos GROUP BY curso"
        },
        {
            "conceito": "order by",
            "categoria": "sql_comandos",
            "descricao": "Ordena o resultado da consulta por uma ou mais colunas",
            "exemplos": "SELECT * FROM alunos ORDER BY nome ASC, idade DESC"
        },
        {
            "conceito": "having",
            "categoria": "sql_comandos",
            "descricao": "Filtro aplicado após GROUP BY (WHERE é antes, HAVING é depois)",
            "exemplos": "SELECT curso, COUNT(*) as total FROM alunos GROUP BY curso HAVING total > 5"
        },
        {
            "conceito": "like",
            "categoria": "sql_comandos",
            "descricao": "Operador para busca por padrão em textos (% = qualquer coisa, _ = um caractere)",
            "exemplos": "SELECT * FROM alunos WHERE nome LIKE 'Ped%'"
        },
        {
            "conceito": "subquery",
            "categoria": "sql_comandos",
            "descricao": "Consulta dentro de outra consulta (consulta aninhada)",
            "exemplos": "SELECT * FROM alunos WHERE curso_id IN (SELECT id FROM cursos WHERE ativo = 1)"
        },
    ]

    # ════════════════════════════════════════════════════════════════
    # 3. SQLITE ESPECÍFICO
    # ════════════════════════════════════════════════════════════════

    conceitos_sqlite = [
        {
            "conceito": "sqlite",
            "categoria": "sqlite",
            "descricao": "Banco de dados leve, embutido, serverless — arquivo único .db",
            "exemplos": "import sqlite3; conn = sqlite3.connect('meu_banco.db')"
        },
        {
            "conceito": "sqlite3 python",
            "categoria": "sqlite",
            "descricao": "Módulo nativo do Python para trabalhar com SQLite (já vem instalado!)",
            "exemplos": "import sqlite3; conn = sqlite3.connect(':memory:')"
        },
        {
            "conceito": "connection",
            "categoria": "sqlite",
            "descricao": "Objeto de conexão com o banco — porta de entrada para o SQLite",
            "exemplos": "conn = sqlite3.connect('banco.db'); conn.close()"
        },
        {
            "conceito": "cursor",
            "categoria": "sqlite",
            "descricao": "Objeto que executa comandos SQL e navega pelos resultados",
            "exemplos": "cur = conn.cursor(); cur.execute('SELECT * FROM tabela')"
        },
        {
            "conceito": "commit",
            "categoria": "sqlite",
            "descricao": "Salva as alterações no banco — sem commit os dados se perdem!",
            "exemplos": "conn.commit()  # SEMPRE após INSERT, UPDATE, DELETE"
        },
        {
            "conceito": "fetchone fetchall",
            "categoria": "sqlite",
            "descricao": "Métodos para recuperar resultados: fetchone() = 1 registro, fetchall() = todos",
            "exemplos": "cur.execute('SELECT * FROM alunos'); todos = cur.fetchall()"
        },
        {
            "conceito": "parametros sql",
            "categoria": "sqlite",
            "descricao": "Usar ? ou :nome para evitar SQL Injection (NUNCA concatenar strings!)",
            "exemplos": "cur.execute('SELECT * FROM alunos WHERE id = ?', (id_aluno,))"
        },
        {
            "conceito": "row_factory",
            "categoria": "sqlite",
            "descricao": "Configuração que define como os resultados são retornados (dict, tuple, etc)",
            "exemplos": "conn.row_factory = sqlite3.Row  # acessar por nome da coluna"
        },
        {
            "conceito": "tipos sqlite",
            "categoria": "sqlite",
            "descricao": "SQLite usa tipos dinâmicos: NULL, INTEGER, REAL, TEXT, BLOB",
            "exemplos": "INTEGER = números inteiros, REAL = decimais, TEXT = strings, BLOB = binários"
        },
        {
            "conceito": "autoincrement",
            "categoria": "sqlite",
            "descricao": "Gera IDs automáticos incrementais para chave primária",
            "exemplos": "id INTEGER PRIMARY KEY AUTOINCREMENT"
        },
        {
            "conceito": "transação",
            "categoria": "sqlite",
            "descricao": "Conjunto de operações atômicas — ou todas executam, ou nenhuma",
            "exemplos": "BEGIN TRANSACTION; INSERT...; UPDATE...; COMMIT; (ou ROLLBACK se der erro)"
        },
        {
            "conceito": "context manager sqlite",
            "categoria": "sqlite",
            "descricao": "Usar 'with' para garantir que conexão seja fechada automaticamente",
            "exemplos": "with sqlite3.connect('banco.db') as conn: conn.execute(...)"
        },
    ]

    # ════════════════════════════════════════════════════════════════
    # 4. CONCEITOS AVANÇADOS
    # ════════════════════════════════════════════════════════════════

    conceitos_avancados = [
        {
            "conceito": "acid",
            "categoria": "avancado",
            "descricao": "Propriedades de transação: Atomicidade, Consistência, Isolamento, Durabilidade",
            "exemplos": "SQLite é ACID compliant — garante integridade dos dados"
        },
        {
            "conceito": "sql injection",
            "categoria": "avancado",
            "descricao": "Ataque que injeta código SQL malicioso — SEMPRE use parâmetros!",
            "exemplos": "ERRADO: f'SELECT * FROM x WHERE id={input}' | CERTO: cursor.execute('...WHERE id=?', (input,))"
        },
        {
            "conceito": "orm",
            "categoria": "avancado",
            "descricao": "Object-Relational Mapping — mapeia objetos Python para tabelas SQL",
            "exemplos": "SQLAlchemy, Peewee, Django ORM"
        },
        {
            "conceito": "view",
            "categoria": "avancado",
            "descricao": "Tabela virtual baseada em uma consulta SELECT salva",
            "exemplos": "CREATE VIEW alunos_ativos AS SELECT * FROM alunos WHERE ativo = 1"
        },
        {
            "conceito": "trigger",
            "categoria": "avancado",
            "descricao": "Código SQL que executa automaticamente quando algo acontece na tabela",
            "exemplos": "CREATE TRIGGER log_insert AFTER INSERT ON alunos BEGIN INSERT INTO log...; END"
        },
        {
            "conceito": "explain query plan",
            "categoria": "avancado",
            "descricao": "Mostra como o SQLite vai executar uma consulta (otimização)",
            "exemplos": "EXPLAIN QUERY PLAN SELECT * FROM alunos WHERE nome = 'Pedro'"
        },
    ]

    # ── Inserir todos os conceitos ──────────────────────────────────

    todas_listas = [
        conceitos_fundamentos, conceitos_sql,
        conceitos_sqlite, conceitos_avancados
    ]

    total = 0
    for lista in todas_listas:
        for c in lista:
            cerebro.aprender(**c)
            total += 1

    print(f"\n[OK] {total} conceitos carregados no cerebro!")

    # ════════════════════════════════════════════════════════════════
    # 5. CRIAR SINAPSES (conexões entre conceitos)
    # ════════════════════════════════════════════════════════════════

    print("\n[LINK] Criando conexoes sinapticas...")

    conexoes = [
        # Fundamentos
        ("banco de dados", "sgbd", "requer"),
        ("banco de dados", "modelo relacional", "usa"),
        ("modelo relacional", "tabela", "composto_por"),
        ("tabela", "registro", "contém"),
        ("tabela", "campo", "contém"),
        ("tabela", "chave primária", "possui"),
        ("tabela", "chave estrangeira", "pode_ter"),
        ("chave estrangeira", "chave primária", "referencia"),
        ("tabela", "índice", "pode_ter"),
        ("normalização", "tabela", "organiza"),

        # SQL ↔ Fundamentos
        ("select", "where", "usa_com"),
        ("select", "join", "usa_com"),
        ("select", "group by", "usa_com"),
        ("select", "order by", "usa_com"),
        ("select", "having", "usa_com"),
        ("select", "like", "usa_com"),
        ("select", "subquery", "pode_ter"),
        ("insert", "registro", "cria"),
        ("update", "registro", "modifica"),
        ("delete", "registro", "remove"),
        ("create table", "tabela", "cria"),
        ("alter table", "tabela", "modifica"),
        ("drop table", "tabela", "remove"),

        # SQLite
        ("sqlite", "banco de dados", "é_um"),
        ("sqlite", "sqlite3 python", "usa"),
        ("sqlite3 python", "connection", "cria"),
        ("connection", "cursor", "cria"),
        ("cursor", "select", "executa"),
        ("cursor", "insert", "executa"),
        ("cursor", "update", "executa"),
        ("cursor", "delete", "executa"),
        ("connection", "commit", "precisa"),
        ("cursor", "fetchone fetchall", "usa"),
        ("sqlite", "tipos sqlite", "possui"),
        ("sqlite", "transação", "suporta"),
        ("sqlite", "autoincrement", "suporta"),
        ("parametros sql", "sql injection", "previne"),
        ("context manager sqlite", "connection", "gerencia"),

        # Avançados
        ("transação", "acid", "segue"),
        ("sqlite", "acid", "implementa"),
        ("orm", "sqlite", "abstrai"),
        ("view", "select", "salva"),
        ("trigger", "tabela", "monitora"),
        ("explain query plan", "select", "analisa"),
        ("índice", "explain query plan", "otimiza"),
    ]

    for origem, destino, tipo in conexoes:
        cerebro.conectar(origem, destino, tipo)

    print(f"[OK] {len(conexoes)} conexoes sinapticas criadas!")

    # ════════════════════════════════════════════════════════════════
    # 6. CRIAR FLASHCARDS PARA ESTUDO
    # ════════════════════════════════════════════════════════════════

    print("\n[CARD] Criando flashcards de estudo...")

    flashcards = [
        # Fundamentos
        ("banco de dados", "O que é um banco de dados?",
         "Coleção organizada de dados estruturados, armazenados eletronicamente, que permite criar, ler, atualizar e deletar informações (CRUD).", 1),

        ("sgbd", "O que é um SGBD? Cite 3 exemplos.",
         "Sistema Gerenciador de Banco de Dados — software que gerencia o acesso aos dados. Ex: MySQL, PostgreSQL, SQLite.", 1),

        ("modelo relacional", "O que é o modelo relacional?",
         "Modelo que organiza dados em tabelas (relações) com linhas (registros) e colunas (campos), relacionadas por chaves.", 1),

        ("chave primária", "O que é uma chave primária (PRIMARY KEY)?",
         "Campo que identifica unicamente cada registro na tabela. Não pode ser NULL nem repetido.", 1),

        ("chave estrangeira", "O que é uma chave estrangeira (FOREIGN KEY)?",
         "Campo que referencia a chave primária de OUTRA tabela, criando um relacionamento entre elas.", 2),

        ("normalização", "O que é normalização e quais são as formas normais?",
         "Processo de organizar tabelas para eliminar redundância. 1FN: sem campos multivalorados. 2FN: cada campo depende da PK inteira. 3FN: sem dependências transitivas.", 3),

        # SQL
        ("select", "Escreva um SELECT que busca alunos maiores de 18 anos ordenados por nome.",
         "SELECT nome, idade FROM alunos WHERE idade > 18 ORDER BY nome ASC;", 1),

        ("insert", "Como inserir um registro na tabela alunos?",
         "INSERT INTO alunos (nome, idade, curso) VALUES ('Pedro', 20, 'TI');", 1),

        ("update", "Como atualizar a idade de um aluno específico?",
         "UPDATE alunos SET idade = 21 WHERE id = 1;  (SEMPRE use WHERE para não alterar todos!)", 1),

        ("delete", "Como deletar um registro de forma segura?",
         "DELETE FROM alunos WHERE id = 5;  (SEMPRE use WHERE! Sem WHERE deleta TUDO!)", 1),

        ("join", "Qual a diferença entre INNER JOIN, LEFT JOIN e RIGHT JOIN?",
         "INNER JOIN: só registros que existem nas DUAS tabelas. LEFT JOIN: todos da esquerda + correspondentes da direita. RIGHT JOIN: inverso do LEFT.", 2),

        ("group by", "Escreva uma query que conta quantos alunos tem em cada curso.",
         "SELECT curso, COUNT(*) as total FROM alunos GROUP BY curso;", 2),

        ("having", "Qual a diferença entre WHERE e HAVING?",
         "WHERE filtra ANTES do agrupamento (linhas individuais). HAVING filtra DEPOIS do GROUP BY (grupos). HAVING funciona com funções de agregação.", 2),

        ("subquery", "O que é uma subquery? Dê um exemplo.",
         "Consulta dentro de outra consulta. Ex: SELECT * FROM alunos WHERE curso_id IN (SELECT id FROM cursos WHERE ativo = 1)", 3),

        # SQLite
        ("sqlite", "Quais são as vantagens do SQLite?",
         "1) Serverless (sem servidor). 2) Arquivo único .db. 3) Zero configuração. 4) Já vem com Python. 5) ACID compliant. 6) Perfeito para apps locais e protótipos.", 1),

        ("sqlite3 python", "Como conectar ao SQLite usando Python?",
         "import sqlite3\nconn = sqlite3.connect('meu_banco.db')  # arquivo\nconn = sqlite3.connect(':memory:')  # em memória (temporário)", 1),

        ("cursor", "Para que serve o cursor no SQLite?",
         "O cursor é o objeto que executa comandos SQL e navega pelos resultados. Criado com: cur = conn.cursor(); cur.execute('SELECT...')", 1),

        ("commit", "Quando você DEVE usar conn.commit()?",
         "SEMPRE após INSERT, UPDATE ou DELETE! Sem commit, as alterações ficam em memória e se perdem ao fechar a conexão.", 1),

        ("fetchone fetchall", "Qual a diferença entre fetchone() e fetchall()?",
         "fetchone() retorna UM registro (ou None). fetchall() retorna TODOS os registros como lista de tuplas.", 1),

        ("parametros sql", "Por que usar parâmetros (?) em vez de f-strings no SQL?",
         "Para prevenir SQL Injection! ERRADO: f\"WHERE id={x}\". CERTO: cursor.execute('WHERE id=?', (x,)). Parâmetros são sanitizados automaticamente.", 2),

        ("tipos sqlite", "Quais são os 5 tipos de dados do SQLite?",
         "NULL (nulo), INTEGER (inteiro), REAL (decimal/float), TEXT (string), BLOB (dados binários). SQLite usa tipagem dinâmica!", 1),

        ("transação", "O que é uma transação no banco de dados?",
         "Conjunto de operações atômicas — ou TODAS executam com sucesso (COMMIT), ou NENHUMA executa (ROLLBACK). Garante integridade dos dados.", 2),

        # Avançados
        ("acid", "O que significa ACID em bancos de dados?",
         "A=Atomicidade (tudo ou nada), C=Consistência (dados válidos), I=Isolamento (transações independentes), D=Durabilidade (dados persistem após commit).", 3),

        ("sql injection", "O que é SQL Injection e como prevenir?",
         "Ataque onde input malicioso é interpretado como SQL. Prevenir: SEMPRE usar parâmetros (?) e NUNCA concatenar strings com input do usuário.", 2),

        ("view", "O que é uma VIEW no SQL?",
         "Tabela virtual baseada em um SELECT salvo. Não armazena dados, apenas a consulta. CREATE VIEW ativos AS SELECT * FROM alunos WHERE ativo=1;", 2),

        ("trigger", "O que é um TRIGGER?",
         "Código SQL que executa automaticamente quando algo acontece (INSERT, UPDATE, DELETE). Útil para logs e validações automáticas.", 3),

        ("create table", "Escreva um CREATE TABLE completo para uma tabela de produtos.",
         "CREATE TABLE IF NOT EXISTS produtos (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  nome TEXT NOT NULL,\n  preco REAL DEFAULT 0.0,\n  estoque INTEGER DEFAULT 0,\n  criado_em TEXT DEFAULT CURRENT_TIMESTAMP\n);", 1),

        ("índice", "Quando criar um índice e qual o trade-off?",
         "Criar índice em colunas usadas frequentemente em WHERE/JOIN. Trade-off: acelera leituras mas DESACELERA escrita (INSERT/UPDATE) pois precisa atualizar o índice.", 3),
    ]

    for conceito, pergunta, resposta, dificuldade in flashcards:
        cerebro.criar_flashcard(conceito, pergunta, resposta, dificuldade)

    print(f"[OK] {len(flashcards)} flashcards criados!")
    print("\n" + "=" * 60)
    print("Base de conhecimento carregada com sucesso!")
    print("=" * 60)


# ── Execução direta ───────────────────────────────────────────────────

if __name__ == "__main__":
    cerebro = CerebroFaux()
    carregar_conhecimento_sql(cerebro)
    cerebro.mapa_mental()
    cerebro.salvar()
    cerebro.fechar()
