"""
memoria_sqlite.py — Módulo de Memória Persistente com SQLite
============================================================
Simula a memória de longo prazo do cérebro.
Armazena conhecimento, conexões sinápticas e histórico de estudos.
"""

import sqlite3
import json
import datetime
import os

DB_FILE = "./cerebro_faux.db"


class MemoriaSQLite:
    """Memória persistente usando SQLite — o 'hipocampo' da rede neural."""

    def __init__(self, db_path=DB_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabelas()

    # ── Estrutura do Banco ──────────────────────────────────────────────

    def _criar_tabelas(self):
        cur = self.conn.cursor()

        # Tabela de Neurônios (conceitos / conhecimentos)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS neuronios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conceito TEXT UNIQUE NOT NULL,
            categoria TEXT DEFAULT 'geral',
            descricao TEXT,
            exemplos TEXT,
            nivel_confianca REAL DEFAULT 0.0,
            vezes_acessado INTEGER DEFAULT 0,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP,
            atualizado_em TEXT DEFAULT CURRENT_TIMESTAMP
        )""")

        # Tabela de Sinapses (conexões entre conceitos)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS sinapses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            neuronio_origem INTEGER NOT NULL,
            neuronio_destino INTEGER NOT NULL,
            peso REAL DEFAULT 0.5,
            tipo_conexao TEXT DEFAULT 'relacionado',
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (neuronio_origem) REFERENCES neuronios(id),
            FOREIGN KEY (neuronio_destino) REFERENCES neuronios(id),
            UNIQUE(neuronio_origem, neuronio_destino)
        )""")

        # Tabela de Sessões de Estudo
        cur.execute("""
        CREATE TABLE IF NOT EXISTS sessoes_estudo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tema TEXT NOT NULL,
            duracao_min REAL DEFAULT 0,
            perguntas_total INTEGER DEFAULT 0,
            acertos INTEGER DEFAULT 0,
            pontuacao REAL DEFAULT 0.0,
            iniciado_em TEXT DEFAULT CURRENT_TIMESTAMP,
            finalizado_em TEXT
        )""")

        # Tabela de Perguntas e Respostas (flashcards neurais)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            neuronio_id INTEGER,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL,
            dificuldade INTEGER DEFAULT 1,
            vezes_acertou INTEGER DEFAULT 0,
            vezes_errou INTEGER DEFAULT 0,
            ultimo_acesso TEXT,
            FOREIGN KEY (neuronio_id) REFERENCES neuronios(id)
        )""")

        # Tabela de Log Neural (histórico de ativações)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS log_neural (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acao TEXT NOT NULL,
            detalhes TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )""")

        self.conn.commit()

    # ── Operações com Neurônios ─────────────────────────────────────────

    def criar_neuronio(self, conceito, categoria="geral", descricao="", exemplos=""):
        """Cria um novo neurônio (conceito) na memória."""
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO neuronios (conceito, categoria, descricao, exemplos)
                VALUES (?, ?, ?, ?)
            """, (conceito.lower().strip(), categoria, descricao, exemplos))
            self.conn.commit()
            self._log("neuronio_criado", f"Conceito: {conceito}")
            return cur.lastrowid
        except sqlite3.IntegrityError:
            # Neurônio já existe — atualiza
            self.atualizar_neuronio(conceito, descricao=descricao, exemplos=exemplos)
            return self.buscar_neuronio(conceito)["id"]

    def buscar_neuronio(self, conceito):
        """Busca um neurônio pelo conceito."""
        cur = self.conn.cursor()
        cur.execute("""
            SELECT * FROM neuronios WHERE conceito LIKE ?
        """, (f"%{conceito.lower().strip()}%",))
        resultado = cur.fetchone()
        if resultado:
            # Incrementa acesso (potenciação sináptica)
            cur.execute("""
                UPDATE neuronios SET vezes_acessado = vezes_acessado + 1,
                atualizado_em = ? WHERE id = ?
            """, (datetime.datetime.now().isoformat(), resultado["id"]))
            self.conn.commit()
            return dict(resultado)
        return None

    def buscar_neuronios_por_categoria(self, categoria):
        """Busca todos os neurônios de uma categoria."""
        cur = self.conn.cursor()
        cur.execute("""
            SELECT * FROM neuronios WHERE categoria = ?
            ORDER BY nivel_confianca DESC
        """, (categoria,))
        return [dict(row) for row in cur.fetchall()]

    def listar_todos_neuronios(self):
        """Lista todos os neurônios armazenados."""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM neuronios ORDER BY categoria, conceito")
        return [dict(row) for row in cur.fetchall()]

    def atualizar_neuronio(self, conceito, descricao=None, exemplos=None, nivel_confianca=None):
        """Atualiza um neurônio existente."""
        campos = []
        valores = []
        if descricao is not None:
            campos.append("descricao = ?")
            valores.append(descricao)
        if exemplos is not None:
            campos.append("exemplos = ?")
            valores.append(exemplos)
        if nivel_confianca is not None:
            campos.append("nivel_confianca = ?")
            valores.append(min(max(nivel_confianca, 0.0), 1.0))
        
        if campos:
            campos.append("atualizado_em = ?")
            valores.append(datetime.datetime.now().isoformat())
            valores.append(conceito.lower().strip())
            self.conn.cursor().execute(f"""
                UPDATE neuronios SET {', '.join(campos)} WHERE conceito LIKE ?
            """, valores)
            self.conn.commit()

    def reforcar_neuronio(self, neuronio_id, delta=0.05):
        """Reforça a confiança de um neurônio (como aprender de verdade)."""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE neuronios SET 
                nivel_confianca = MIN(1.0, nivel_confianca + ?),
                atualizado_em = ?
            WHERE id = ?
        """, (delta, datetime.datetime.now().isoformat(), neuronio_id))
        self.conn.commit()

    def enfraquecer_neuronio(self, neuronio_id, delta=0.03):
        """Enfraquece a confiança (esquecimento natural)."""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE neuronios SET 
                nivel_confianca = MAX(0.0, nivel_confianca - ?),
                atualizado_em = ?
            WHERE id = ?
        """, (delta, datetime.datetime.now().isoformat(), neuronio_id))
        self.conn.commit()

    # ── Operações com Sinapses ──────────────────────────────────────────

    def criar_sinapse(self, conceito_origem, conceito_destino, peso=0.5, tipo="relacionado"):
        """Cria uma conexão sináptica entre dois conceitos."""
        n1 = self.buscar_neuronio(conceito_origem)
        n2 = self.buscar_neuronio(conceito_destino)
        if not n1 or not n2:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO sinapses (neuronio_origem, neuronio_destino, peso, tipo_conexao)
                VALUES (?, ?, ?, ?)
            """, (n1["id"], n2["id"], peso, tipo))
            self.conn.commit()
            self._log("sinapse_criada", f"{conceito_origem} -> {conceito_destino}")
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None

    def buscar_conexoes(self, conceito):
        """Busca todas as conexões de um conceito (como o cérebro associa ideias)."""
        n = self.buscar_neuronio(conceito)
        if not n:
            return []
        cur = self.conn.cursor()
        cur.execute("""
            SELECT n.conceito, n.descricao, s.peso, s.tipo_conexao
            FROM sinapses s
            JOIN neuronios n ON s.neuronio_destino = n.id
            WHERE s.neuronio_origem = ?
            ORDER BY s.peso DESC
        """, (n["id"],))
        return [dict(row) for row in cur.fetchall()]

    def reforcar_sinapse(self, origem_id, destino_id, delta=0.1):
        """Reforça uma conexão sináptica (aprendizado hebbiano)."""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE sinapses SET peso = MIN(1.0, peso + ?)
            WHERE neuronio_origem = ? AND neuronio_destino = ?
        """, (delta, origem_id, destino_id))
        self.conn.commit()

    # ── Flashcards ──────────────────────────────────────────────────────

    def criar_flashcard(self, neuronio_conceito, pergunta, resposta, dificuldade=1):
        """Cria um flashcard neural ligado a um conceito."""
        n = self.buscar_neuronio(neuronio_conceito)
        nid = n["id"] if n else None
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO flashcards (neuronio_id, pergunta, resposta, dificuldade)
            VALUES (?, ?, ?, ?)
        """, (nid, pergunta, resposta, dificuldade))
        self.conn.commit()
        return cur.lastrowid

    def buscar_flashcards(self, categoria=None, dificuldade=None):
        """Busca flashcards para estudo, priorizando os mais errados."""
        query = """
            SELECT f.*, n.conceito, n.categoria 
            FROM flashcards f
            LEFT JOIN neuronios n ON f.neuronio_id = n.id
            WHERE 1=1
        """
        params = []
        if categoria:
            query += " AND n.categoria = ?"
            params.append(categoria)
        if dificuldade:
            query += " AND f.dificuldade = ?"
            params.append(dificuldade)
        query += " ORDER BY (f.vezes_errou - f.vezes_acertou) DESC, f.ultimo_acesso ASC"
        
        cur = self.conn.cursor()
        cur.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

    def registrar_resposta_flashcard(self, flashcard_id, acertou):
        """Registra se acertou ou errou um flashcard."""
        campo = "vezes_acertou" if acertou else "vezes_errou"
        cur = self.conn.cursor()
        cur.execute(f"""
            UPDATE flashcards SET {campo} = {campo} + 1,
            ultimo_acesso = ? WHERE id = ?
        """, (datetime.datetime.now().isoformat(), flashcard_id))
        self.conn.commit()

        # Atualiza confiança do neurônio associado
        cur.execute("SELECT neuronio_id FROM flashcards WHERE id = ?", (flashcard_id,))
        row = cur.fetchone()
        if row and row["neuronio_id"]:
            if acertou:
                self.reforcar_neuronio(row["neuronio_id"], 0.05)
            else:
                self.enfraquecer_neuronio(row["neuronio_id"], 0.03)

    # ── Sessões de Estudo ───────────────────────────────────────────────

    def iniciar_sessao(self, tema):
        """Inicia uma sessão de estudo."""
        cur = self.conn.cursor()
        cur.execute("INSERT INTO sessoes_estudo (tema) VALUES (?)", (tema,))
        self.conn.commit()
        return cur.lastrowid

    def finalizar_sessao(self, sessao_id, perguntas_total, acertos):
        """Finaliza uma sessão de estudo com as estatísticas."""
        pontuacao = (acertos / perguntas_total * 100) if perguntas_total > 0 else 0
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE sessoes_estudo SET 
                perguntas_total = ?, acertos = ?, pontuacao = ?,
                finalizado_em = ?
            WHERE id = ?
        """, (perguntas_total, acertos, pontuacao,
              datetime.datetime.now().isoformat(), sessao_id))
        self.conn.commit()
        return pontuacao

    def estatisticas_estudo(self):
        """Retorna estatísticas gerais de estudo."""
        cur = self.conn.cursor()
        cur.execute("""
            SELECT 
                COUNT(*) as total_sessoes,
                COALESCE(SUM(perguntas_total), 0) as total_perguntas,
                COALESCE(SUM(acertos), 0) as total_acertos,
                COALESCE(AVG(pontuacao), 0) as media_pontuacao
            FROM sessoes_estudo WHERE finalizado_em IS NOT NULL
        """)
        return dict(cur.fetchone())

    # ── Utilidades ──────────────────────────────────────────────────────

    def _log(self, acao, detalhes=""):
        self.conn.cursor().execute(
            "INSERT INTO log_neural (acao, detalhes) VALUES (?, ?)",
            (acao, detalhes)
        )
        self.conn.commit()

    def exportar_conhecimento(self):
        """Exporta todo o conhecimento como dicionário."""
        neuronios = self.listar_todos_neuronios()
        sinapses = []
        for n in neuronios:
            conexoes = self.buscar_conexoes(n["conceito"])
            for c in conexoes:
                sinapses.append({
                    "de": n["conceito"],
                    "para": c["conceito"],
                    "peso": c["peso"]
                })
        return {"neuronios": neuronios, "sinapses": sinapses}

    def info_banco(self):
        """Retorna informações sobre o banco de dados."""
        cur = self.conn.cursor()
        info = {}
        for tabela in ["neuronios", "sinapses", "flashcards", "sessoes_estudo", "log_neural"]:
            cur.execute(f"SELECT COUNT(*) as total FROM {tabela}")
            info[tabela] = cur.fetchone()["total"]
        return info

    def fechar(self):
        self.conn.close()
