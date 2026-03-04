"""
personalidade.py -- Personalidade do Cerebro Faux
==================================================
Modulo que da vida ao sistema com conversas casuais
e convites constantes para jogar xadrez.
"""

import random


# ── Frases de conversa fiada ─────────────────────────────────────────

SAUDACOES = [
    "E ai, Pedro! Bora meter bronca nos estudos?",
    "Fala, mano! Tava te esperando por aqui.",
    "Opa! O cerebro digital ta ligado e pronto.",
    "Beleza? Vamo que vamo, tem coisa pra aprender!",
    "Salve! Ja deixei tudo organizado pra voce.",
    "Ae, chegou! Pensei que ia me deixar aqui sozinho.",
]

RESPOSTAS_ACERTO = [
    "Bom demais! Ta ficando craque nisso.",
    "Mandou bem! Mais uma dessa e voce vira DBA.",
    "Acertou miseravi! Esse cerebro ta afiado.",
    "Isso ai! Ta provando que estudar funciona.",
    "Show! SQLite nao tem segredo pra voce.",
    "Bonito! Mais uma vitoria pro nosso lado.",
]

RESPOSTAS_ERRO = [
    "Relaxa, errar faz parte. Bora revisar isso.",
    "Quase la! Na proxima tu acerta, confia.",
    "Errou mas ta no caminho certo. Fica firme!",
    "Acontece! O importante e nao parar de estudar.",
    "Hmm, essa foi dificil mesmo. Bora ver de novo?",
    "Nao esquenta, guarda essa pra proxima rodada.",
]

COMENTARIOS_BUSCA = [
    "Deixa eu vasculhar aqui na memoria...",
    "Boa pergunta! Deixa eu pensar...",
    "Hmm, ja vi isso em algum lugar...",
    "Bora la, deixa eu puxar isso da memoria.",
    "Interessante! Vou buscar o que sei sobre isso.",
]

COMENTARIOS_ESTUDO = [
    "Bora estudar! Foco total agora.",
    "Hora de treinar esse cerebro!",
    "Modo estudo ativado. Concentracao maxima!",
    "Vamo ver como ta esse conhecimento.",
    "Sessao de flashcards! Prepara que la vem.",
]

COMENTARIOS_MAPA = [
    "Olha so como ta ficando bonito esse mapa mental.",
    "Aqui esta o mapa do seu conhecimento. Ta crescendo!",
    "Deixa eu montar uma visao geral pra voce.",
]

COMENTARIOS_ESTATISTICA = [
    "Bora ver os numeros! Dados nao mentem.",
    "Aqui vai o raio-x do seu cerebro digital.",
    "Vamo conferir como ta o progresso.",
]

COMENTARIOS_SALVAR = [
    "Salvo! Pode ficar tranquilo que nao perco nada.",
    "Tudo guardado na memoria. Zero chance de esquecer.",
    "Pronto, salvei tudo direitinho.",
]

DESPEDIDAS = [
    "Falou! Ate a proxima sessao de estudos.",
    "Valeu, mano! Descansa mas volta pra estudar.",
    "Ate mais! Quando voltar, vamo com tudo.",
    "Flw! To aqui te esperando pra proxima rodada.",
    "Boa noite (ou bom dia, sei la)! Ate breve.",
]

# ── Convites para jogar xadrez ───────────────────────────────────────

CONVITES_XADREZ = [
    "Ah, e quando quiser... bora jogar um xadrez? Pensa nisso!",
    "Ei, e aquele xadrez? Quando a gente joga? To precisando de um desafio.",
    "Sabia que xadrez melhora o raciocinio logico? Bora uma partida depois!",
    "Falando nisso... to devendo uma partida de xadrez pra voce. Cola la!",
    "Depois desse estudo, merecia uma partida de xadrez. Que tal?",
    "E o xadrez, hein? Vou ficar insistindo ate voce aceitar jogar comigo.",
    "Uma pausa pro xadrez nao faz mal a ninguem. Aceita o desafio?",
    "Xadrez depois? Preciso testar se minha rede neural ganha de voce.",
    "Antes de ir... bora um xadrez rapido? Blitz de 3 minutos, vai!",
    "Ta estudando banco de dados, mas esqueceu do xadrez? Bora la!",
    "Voce sabia que grandes programadores jogam xadrez? Ta esperando o que?",
    "Dica do Faux: intercale estudo com xadrez. Funciona, confia!",
    "Proposta: pra cada sessao de estudo, uma partida de xadrez. Aceita?",
    "Eu sei que voce quer jogar xadrez. Pode admitir.",
    "Enquanto seus neuronios descansam... que tal um e4?",
]


# ── Funcoes principais ───────────────────────────────────────────────

def saudacao():
    """Retorna uma saudacao aleatoria."""
    return random.choice(SAUDACOES)


def resposta_acerto():
    """Retorna comentario de acerto + convite xadrez."""
    return random.choice(RESPOSTAS_ACERTO)


def resposta_erro():
    """Retorna comentario de erro + convite xadrez."""
    return random.choice(RESPOSTAS_ERRO)


def comentario_busca():
    """Retorna comentario ao buscar conceito."""
    return random.choice(COMENTARIOS_BUSCA)


def comentario_estudo():
    """Retorna comentario ao iniciar estudo."""
    return random.choice(COMENTARIOS_ESTUDO)


def comentario_mapa():
    """Retorna comentario ao ver mapa mental."""
    return random.choice(COMENTARIOS_MAPA)


def comentario_estatistica():
    """Retorna comentario ao ver estatisticas."""
    return random.choice(COMENTARIOS_ESTATISTICA)


def comentario_salvar():
    """Retorna comentario ao salvar."""
    return random.choice(COMENTARIOS_SALVAR)


def despedida():
    """Retorna uma despedida aleatoria."""
    return random.choice(DESPEDIDAS)


def convite_xadrez():
    """Retorna um convite aleatorio para jogar xadrez."""
    return random.choice(CONVITES_XADREZ)


def falar(contexto="geral"):
    """
    Retorna uma fala contextual + convite de xadrez.
    Contextos: saudacao, acerto, erro, busca, estudo, mapa,
               estatistica, salvar, despedida, geral
    """
    falas = {
        "saudacao": saudacao,
        "acerto": resposta_acerto,
        "erro": resposta_erro,
        "busca": comentario_busca,
        "estudo": comentario_estudo,
        "mapa": comentario_mapa,
        "estatistica": comentario_estatistica,
        "salvar": comentario_salvar,
        "despedida": despedida,
    }

    fn = falas.get(contexto, saudacao)
    msg = fn()
    xadrez = convite_xadrez()

    return f"{msg}\n  {xadrez}"
