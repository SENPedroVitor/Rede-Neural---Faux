"""
main.py — Interface Interativa do Cérebro Faux
===============================================
Menu principal para interagir com sua rede neural de estudos.
Aprenda, estude, teste e evolua seu conhecimento sobre DB e SQLite.
"""

import os
import sys
import random
import time

from cerebro import CerebroFaux
from estudos_db import carregar_conhecimento_sql
from personalidade import falar, convite_xadrez, resposta_acerto, resposta_erro


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\n  Pressione ENTER para continuar...")


def banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     REDE NEURAL FAUX -- CEREBRO DIGITAL                      ║
║     ======================================                    ║
║     Sistema de Estudos: Bancos de Dados & SQLite             ║
║                                                              ║
║     "Eu nao imito um cerebro. Eu sou um." -- Faux            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)


def menu_principal():
    print("""
┌──────────────────────────────────────┐
│         MENU PRINCIPAL               │
├──────────────────────────────────────┤
│  1 | Estudar (Flashcards)            │
│  2 | Buscar Conceito                 │
│  3 | Mapa Mental                     │
│  4 | Testar Rede Neural              │
│  5 | Adicionar Conhecimento          │
│  6 | Ver Conexoes Sinapticas         │
│  7 | Estatisticas                    │
│  8 | Recarregar Base SQL             │
│  9 | Salvar Cerebro                  │
│  0 | Sair                            │
└──────────────────────────────────────┘
    """)
    return input("  Escolha → ").strip()


# ── Modo Estudo (Flashcards) ──────────────────────────────────────────

def modo_estudo(cerebro):
    limpar_tela()
    print("\nMODO ESTUDO -- Flashcards Neurais")
    print("=" * 50)
    print(f"\n  Faux: {falar('estudo')}")
    
    print("\nCategorias disponíveis:")
    print("  1 │ fundamentos")
    print("  2 │ sql_comandos")
    print("  3 │ sqlite")
    print("  4 │ avancado")
    print("  5 │ TODAS")
    
    escolha_cat = input("\n  Categoria → ").strip()
    cat_map = {"1": "fundamentos", "2": "sql_comandos", "3": "sqlite", "4": "avancado", "5": None}
    categoria = cat_map.get(escolha_cat, None)

    print("\nDificuldade: (1) Fácil  (2) Médio  (3) Difícil  (4) Todas")
    dif = input("  Dificuldade → ").strip()
    dificuldade = int(dif) if dif in ["1", "2", "3"] else None

    flashcards = cerebro.estudar(categoria=categoria, limite=20)
    
    if not flashcards:
        print("\n[AVISO] Nenhum flashcard encontrado! Use 'Recarregar Base SQL' primeiro.")
        pausar()
        return

    random.shuffle(flashcards)
    
    sessao_id = cerebro.memoria.iniciar_sessao(
        f"flashcards_{categoria or 'todas'}"
    )
    acertos = 0
    total = 0

    print(f"\n{len(flashcards)} flashcards para estudar. Digite 'sair' para parar.\n")
    print("─" * 50)

    for i, fc in enumerate(flashcards, 1):
        total += 1
        dif_str = "*" * (fc.get("dificuldade", 1) or 1)
        cat_str = fc.get("categoria", "?")

        print(f"\n  Flashcard {i}/{len(flashcards)} [{cat_str}] {dif_str}")
        print(f"\n  [?] {fc['pergunta']}")
        
        resp = input("\n  Sua resposta (ou ENTER para ver): ").strip()
        
        if resp.lower() == "sair":
            break

        print(f"\n  RESPOSTA CORRETA:")
        print(f"  ─────────────────────")
        for linha in fc["resposta"].split("\n"):
            print(f"  {linha}")

        while True:
            avaliacao = input("\n  Você acertou? (s/n): ").strip().lower()
            if avaliacao in ["s", "n", "sim", "nao", "não"]:
                break
            print("  Digite 's' ou 'n'")

        acertou = avaliacao in ["s", "sim"]
        if acertou:
            acertos += 1
            print(f"  [+] {resposta_acerto()}")
        else:
            print(f"  [-] {resposta_erro()}")
        
        cerebro.responder_flashcard(fc["id"], acertou)
        print("─" * 50)

    # Finaliza sessão
    if total > 0:
        pontuacao = cerebro.memoria.finalizar_sessao(sessao_id, total, acertos)
        print(f"\n{'═' * 50}")
        print(f"  RESULTADO DA SESSAO")
        print(f"  ─────────────────────")
        print(f"  Perguntas: {total}")
        print(f"  Acertos:   {acertos}")
        print(f"  Erros:     {total - acertos}")
        print(f"  Pontuação: {pontuacao:.1f}%")
        
        if pontuacao >= 80:
            print("  Excelente! Seu cerebro esta afiado!")
        elif pontuacao >= 60:
            print("  Bom! Continue praticando!")
        elif pontuacao >= 40:
            print("  Precisa revisar mais. Nao desista!")
        else:
            print("  Estude mais e tente novamente!")
        print(f"{'=' * 50}")
        print(f"\n  Faux: {convite_xadrez()}")

    pausar()


# ── Buscar Conceito ──────────────────────────────────────────────────

def buscar_conceito(cerebro):
    limpar_tela()
    print("\nBUSCAR CONCEITO")
    print("=" * 50)
    print(f"\n  Faux: {falar('busca')}")
    
    termo = input("\n  O que voce quer lembrar? -> ").strip()
    if not termo:
        return

    resultado = cerebro.lembrar(termo)
    
    if resultado:
        print(f"\n  ENCONTRADO!")
        print(f"  ─────────────────────")
        print(f"  Conceito:   {resultado['conceito']}")
        print(f"  Categoria:  {resultado['categoria']}")
        print(f"  Confianca:  {resultado['confianca']}")
        print(f"  Acessos:    {resultado['vezes_acessado']}")
        print(f"\n  Descricao:")
        print(f"  {resultado['descricao']}")
        print(f"\n  Exemplos:")
        print(f"  {resultado['exemplos']}")
        
        if resultado['conexoes']:
            print(f"\n  Conexoes:")
            for c in resultado['conexoes']:
                print(f"    → {c}")
    else:
        print(f"\n  Conceito '{termo}' nao encontrado na memoria.")
        print("  Dica: tente termos como 'select', 'sqlite', 'join', 'chave primaria'")

    print(f"\n  Faux: {convite_xadrez()}")
    pausar()


# ── Testar Rede Neural ──────────────────────────────────────────────

def testar_rede_neural(cerebro):
    limpar_tela()
    print("\nTESTE DA REDE NEURAL")
    print("=" * 50)
    
    print("\n  Demonstração: Treinando a rede para aprender XOR")
    print("  (Problema clássico — não-linear)")
    print()

    from rede_neural import RedeNeural

    rede_xor = RedeNeural([2, 4, 1], funcao_ativacao="sigmoid", taxa_aprendizado=0.5)
    
    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [[0], [1], [1], [0]]

    print("  Treinando...")
    rede_xor.treinar(entradas, saidas, epocas=5000, verbose=True)

    print("\n  Resultados apos treinamento:")
    print("  ─────────────────────────────")
    for e, s in zip(entradas, saidas):
        pred = rede_xor.predizer(e)
        correto = "[OK]" if abs(pred[0] - s[0]) < 0.3 else "[X]"
        print(f"  {correto} Input: {e} -> Saida: {pred[0]:.4f} (esperado: {s[0]})")

    info = rede_xor.info()
    print(f"\n  Arquitetura: {info['arquitetura']}")
    print(f"  Total neurônios: {info['total_neuronios']}")
    print(f"  Total parâmetros: {info['total_parametros']}")
    print(f"  Épocas treinadas: {info['epocas_treinadas']}")

    print("\n  ─────────────────────────────")
    print("  Demonstração: Treinando para reconhecer padrões SQL")
    
    # Simula classificação de tipo de comando SQL
    # Input encoding: [tem_SELECT, tem_FROM, tem_WHERE, tem_INSERT, tem_INTO, 
    #                  tem_UPDATE, tem_SET, tem_DELETE, tem_CREATE, tem_TABLE]
    # Output: [é_consulta, é_inserção, é_atualização, é_deleção, é_DDL]

    rede_sql = RedeNeural([10, 16, 8, 5], funcao_ativacao="sigmoid", taxa_aprendizado=0.3)

    dados_sql_in = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # SELECT FROM WHERE → consulta
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # SELECT FROM → consulta
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # INSERT INTO → inserção
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # UPDATE SET → atualização
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],  # UPDATE SET WHERE → atualização (com flag DELETE como WHERE)
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # DELETE → deleção
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # CREATE TABLE → DDL
    ]
    dados_sql_out = [
        [1, 0, 0, 0, 0],  # consulta
        [1, 0, 0, 0, 0],  # consulta
        [0, 1, 0, 0, 0],  # inserção
        [0, 0, 1, 0, 0],  # atualização
        [0, 0, 1, 0, 0],  # atualização
        [0, 0, 0, 1, 0],  # deleção
        [0, 0, 0, 0, 1],  # DDL
    ]

    print("\n  Treinando classificador SQL...")
    rede_sql.treinar(dados_sql_in, dados_sql_out, epocas=3000, verbose=True)

    labels = ["Consulta", "Inserção", "Atualização", "Deleção", "DDL"]
    testes = [
        ([1, 1, 1, 0, 0, 0, 0, 0, 0, 0], "SELECT...FROM...WHERE"),
        ([0, 0, 0, 1, 1, 0, 0, 0, 0, 0], "INSERT INTO"),
        ([0, 0, 0, 0, 0, 1, 1, 0, 0, 0], "UPDATE...SET"),
        ([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], "DELETE"),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1], "CREATE TABLE"),
    ]

    print("\n  Classificacao de comandos SQL:")
    print("  ─────────────────────────────────")
    for inp, desc in testes:
        pred = rede_sql.predizer(inp)
        idx_max = pred.index(max(pred))
        confianca = pred[idx_max]
        print(f"  {desc:<25} → {labels[idx_max]} ({confianca*100:.1f}%)")

    # Salva a rede SQL como o cérebro principal
    cerebro.rede = rede_sql
    cerebro.salvar()
    print("\n  Rede neural SQL salva como cerebro principal!")

    pausar()


# ── Adicionar Conhecimento ───────────────────────────────────────────

def adicionar_conhecimento(cerebro):
    limpar_tela()
    print("\n[+] ADICIONAR CONHECIMENTO")
    print("=" * 50)
    
    print("\n  O que deseja adicionar?")
    print("  1 │ Novo conceito")
    print("  2 │ Nova conexão entre conceitos")
    print("  3 │ Novo flashcard")
    
    escolha = input("\n  Escolha → ").strip()
    
    if escolha == "1":
        conceito = input("\n  Conceito: ").strip()
        print("  Categorias: fundamentos, sql_comandos, sqlite, avancado, geral")
        categoria = input("  Categoria: ").strip() or "geral"
        descricao = input("  Descrição: ").strip()
        exemplos = input("  Exemplos:  ").strip()
        cerebro.aprender(conceito, categoria, descricao, exemplos)

    elif escolha == "2":
        c1 = input("\n  Conceito origem:  ").strip()
        c2 = input("  Conceito destino: ").strip()
        tipo = input("  Tipo de relação (ex: relacionado, requer, usa): ").strip() or "relacionado"
        cerebro.conectar(c1, c2, tipo)

    elif escolha == "3":
        conceito = input("\n  Conceito relacionado: ").strip()
        pergunta = input("  Pergunta: ").strip()
        resposta = input("  Resposta: ").strip()
        dif = input("  Dificuldade (1-3): ").strip()
        dificuldade = int(dif) if dif in ["1", "2", "3"] else 1
        cerebro.criar_flashcard(conceito, pergunta, resposta, dificuldade)

    pausar()


# ── Ver Conexões ─────────────────────────────────────────────────────

def ver_conexoes(cerebro):
    limpar_tela()
    print("\nCONEXOES SINAPTICAS")
    print("=" * 50)
    
    termo = input("\n  Conceito para ver conexões → ").strip()
    if termo:
        cerebro.associar(termo)
    pausar()


# ── Estatísticas ─────────────────────────────────────────────────────

def mostrar_estatisticas(cerebro):
    limpar_tela()
    print("\nESTATISTICAS DO CEREBRO")
    print("=" * 50)
    print(f"\n  Faux: {falar('estatistica')}")
    
    status = cerebro.status()
    
    print(f"\n  MEMORIA")
    print(f"  ─────────────────────")
    print(f"  Neurônios (conceitos):  {status['memoria']['neuronios']}")
    print(f"  Sinapses (conexões):    {status['memoria']['sinapses']}")
    print(f"  Flashcards:             {status['memoria']['flashcards']}")
    print(f"  Sessões de estudo:      {status['memoria']['sessoes']}")
    print(f"  Logs de atividade:      {status['memoria']['logs']}")

    print(f"\n  REDE NEURAL")
    print(f"  ─────────────────────")
    ri = status['rede_neural']
    print(f"  Arquitetura:            {ri['arquitetura']}")
    print(f"  Total camadas:          {ri['total_camadas']}")
    print(f"  Total neurônios:        {ri['total_neuronios']}")
    print(f"  Total parâmetros:       {ri['total_parametros']}")
    print(f"  Épocas treinadas:       {ri['epocas_treinadas']}")

    print(f"\n  ESTUDOS")
    print(f"  ─────────────────────")
    es = status['estudos']
    print(f"  Total sessões:          {es['total_sessoes']}")
    print(f"  Total perguntas:        {es['total_perguntas']}")
    print(f"  Total acertos:          {es['total_acertos']}")
    print(f"  Média de pontuação:     {es['media_pontuacao']:.1f}%")

    pausar()


# ── Loop Principal ───────────────────────────────────────────────────

def main():
    limpar_tela()
    banner()
    
    print("  Inicializando cérebro...")
    cerebro = CerebroFaux()
    
    # Verifica se a base já tem conceitos
    info = cerebro.memoria.info_banco()
    if info["neuronios"] == 0:
        print("\n  Primeira execucao detectada!")
        print("  Carregando base de conhecimento SQL...")
        carregar_conhecimento_sql(cerebro)
        cerebro.salvar()

    print(f"\n  [OK] Cerebro ativo com {info['neuronios']} conceitos e {info['flashcards']} flashcards!")
    print(f"\n  Faux: {falar('saudacao')}")
    pausar()

    while True:
        limpar_tela()
        banner()
        escolha = menu_principal()

        if escolha == "1":
            modo_estudo(cerebro)
        elif escolha == "2":
            buscar_conceito(cerebro)
        elif escolha == "3":
            limpar_tela()
            print(f"\n  Faux: {falar('mapa')}")
            print("\n  Escolha categoria:")
            print("  1-fundamentos  2-sql_comandos  3-sqlite  4-avancado  5-todas")
            cat = input("  → ").strip()
            cat_map = {"1": "fundamentos", "2": "sql_comandos", "3": "sqlite", "4": "avancado"}
            cerebro.mapa_mental(cat_map.get(cat, None))
            pausar()
        elif escolha == "4":
            testar_rede_neural(cerebro)
        elif escolha == "5":
            adicionar_conhecimento(cerebro)
        elif escolha == "6":
            ver_conexoes(cerebro)
        elif escolha == "7":
            mostrar_estatisticas(cerebro)
        elif escolha == "8":
            limpar_tela()
            print("\n  Recarregando base de conhecimento SQL...")
            carregar_conhecimento_sql(cerebro)
            cerebro.salvar()
            pausar()
        elif escolha == "9":
            cerebro.salvar()
            print(f"  Faux: {falar('salvar')}")
            pausar()
        elif escolha == "0":
            cerebro.salvar()
            cerebro.fechar()
            print(f"\n  Faux: {falar('despedida')}")
            break
        else:
            print("  Opcao invalida!")
            time.sleep(1)


if __name__ == "__main__":
    main()
