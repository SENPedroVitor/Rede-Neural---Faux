"""
cerebro.py — Cérebro Digital Faux (Integração Completa)
=======================================================
Combina a rede neural com a memória SQLite para criar
um sistema cognitivo unificado que aprende e evolui.
"""

import os
import datetime
from memoria_sqlite import MemoriaSQLite
from rede_neural import RedeNeural


class CerebroFaux:
    """
    O Cérebro Digital — integra rede neural + memória SQLite.
    
    Componentes (análogos ao cérebro humano):
    - Memória SQLite → Hipocampo (memória de longo prazo)
    - Rede Neural    → Córtex (processamento e reconhecimento de padrões)
    - Sinapses       → Conexões associativas entre conceitos
    - Flashcards     → Sistema de revisão espaçada (repetição)
    """

    def __init__(self):
        self.memoria = MemoriaSQLite()
        self.rede = None
        self._carregar_ou_criar_rede()
        print("🧠 Cérebro Faux inicializado!")

    def _carregar_ou_criar_rede(self):
        """Tenta carregar rede existente ou cria uma nova."""
        self.rede = RedeNeural.carregar("rede_neural_faux.json")
        if self.rede is None:
            # Rede padrão: 10 entradas, 2 camadas ocultas, 5 saídas
            self.rede = RedeNeural([10, 16, 8, 5], funcao_ativacao="sigmoid", taxa_aprendizado=0.1)
            print("🆕 Nova rede neural criada: [10 → 16 → 8 → 5]")

    # ── Aprender Conceito ──────────────────────────────────────────────

    def aprender(self, conceito, categoria="geral", descricao="", exemplos=""):
        """
        Aprende um novo conceito — cria neurônio na memória.
        
        Returns:
            ID do neurônio criado
        """
        nid = self.memoria.criar_neuronio(conceito, categoria, descricao, exemplos)
        self.memoria._log("aprendizado", f"Aprendeu: {conceito} [{categoria}]")
        print(f"✅ Conceito aprendido: '{conceito}' (categoria: {categoria})")
        return nid

    def conectar(self, conceito1, conceito2, tipo="relacionado"):
        """Cria conexão sináptica entre dois conceitos."""
        sid = self.memoria.criar_sinapse(conceito1, conceito2, tipo=tipo)
        if sid:
            print(f"🔗 Sinapse criada: '{conceito1}' ↔ '{conceito2}' ({tipo})")
        else:
            print(f"⚠️  Não foi possível conectar (conceitos existem?)")
        return sid

    def lembrar(self, conceito):
        """
        Tenta lembrar de um conceito — busca na memória.
        Simula o processo de recall cerebral.
        """
        n = self.memoria.buscar_neuronio(conceito)
        if n:
            conexoes = self.memoria.buscar_conexoes(conceito)
            resultado = {
                "conceito": n["conceito"],
                "categoria": n["categoria"],
                "descricao": n["descricao"],
                "exemplos": n["exemplos"],
                "confianca": f"{n['nivel_confianca'] * 100:.1f}%",
                "vezes_acessado": n["vezes_acessado"],
                "conexoes": [
                    f"{c['conceito']} (peso: {c['peso']:.2f}, tipo: {c['tipo_conexao']})"
                    for c in conexoes
                ]
            }
            return resultado
        return None

    def associar(self, conceito):
        """Busca associações de um conceito (pensamento associativo)."""
        conexoes = self.memoria.buscar_conexoes(conceito)
        if conexoes:
            print(f"\n🔗 Associações de '{conceito}':")
            for c in conexoes:
                barra = "█" * int(c["peso"] * 10)
                print(f"  → {c['conceito']}: {barra} ({c['peso']:.2f}) [{c['tipo_conexao']}]")
        else:
            print(f"  Nenhuma conexão encontrada para '{conceito}'")
        return conexoes

    # ── Sistema de Estudos ─────────────────────────────────────────────

    def criar_flashcard(self, conceito, pergunta, resposta, dificuldade=1):
        """Cria um flashcard para estudo."""
        fid = self.memoria.criar_flashcard(conceito, pergunta, resposta, dificuldade)
        print(f"📝 Flashcard criado para '{conceito}'")
        return fid

    def estudar(self, categoria=None, limite=10):
        """
        Modo de estudo com flashcards.
        Retorna lista de flashcards priorizados (mais difíceis primeiro).
        """
        flashcards = self.memoria.buscar_flashcards(categoria=categoria)
        return flashcards[:limite]

    def responder_flashcard(self, flashcard_id, acertou):
        """Registra resposta de flashcard e atualiza memória."""
        self.memoria.registrar_resposta_flashcard(flashcard_id, acertou)

    # ── Visão Geral ────────────────────────────────────────────────────

    def status(self):
        """Retorna status completo do cérebro."""
        info_db = self.memoria.info_banco()
        info_rede = self.rede.info()
        stats = self.memoria.estatisticas_estudo()

        return {
            "memoria": {
                "neuronios": info_db["neuronios"],
                "sinapses": info_db["sinapses"],
                "flashcards": info_db["flashcards"],
                "sessoes": info_db["sessoes_estudo"],
                "logs": info_db["log_neural"]
            },
            "rede_neural": info_rede,
            "estudos": stats
        }

    def mapa_mental(self, categoria=None):
        """Gera um mapa mental dos conceitos armazenados."""
        if categoria:
            neuronios = self.memoria.buscar_neuronios_por_categoria(categoria)
        else:
            neuronios = self.memoria.listar_todos_neuronios()

        if not neuronios:
            print("  (nenhum conceito armazenado)")
            return

        # Agrupa por categoria
        categorias = {}
        for n in neuronios:
            cat = n["categoria"]
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(n)

        print("\n" + "=" * 60)
        print("  🗺️  MAPA MENTAL — CÉREBRO FAUX")
        print("=" * 60)

        for cat, itens in categorias.items():
            print(f"\n  📂 {cat.upper()}")
            print(f"  {'─' * 40}")
            for n in itens:
                confianca = n["nivel_confianca"]
                barra = "█" * int(confianca * 20) + "░" * (20 - int(confianca * 20))
                emoji = "🟢" if confianca > 0.7 else "🟡" if confianca > 0.3 else "🔴"
                print(f"  {emoji} {n['conceito']:<25} [{barra}] {confianca*100:.0f}%")
                if n["descricao"]:
                    print(f"     └─ {n['descricao'][:60]}")

    def salvar(self):
        """Salva o estado do cérebro."""
        self.rede.salvar("rede_neural_faux.json")
        print("💾 Cérebro salvo!")

    def fechar(self):
        """Fecha conexões."""
        self.memoria.fechar()
        print("👋 Cérebro desligado.")
