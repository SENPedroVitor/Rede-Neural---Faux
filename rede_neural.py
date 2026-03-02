"""
rede_neural.py — Rede Neural Artificial Pura (sem frameworks pesados)
=====================================================================
Implementação de uma rede neural feedforward do zero usando apenas math.
Simula como seu cérebro aprende: camadas de neurônios, pesos, bias, ativações.
"""

import math
import random
import json
import os

# Seed para reprodutibilidade
random.seed(42)


# ── Funções de Ativação (como neurotransmissores) ──────────────────────

def sigmoid(x):
    """Função sigmoide — simula ativação neuronal suave."""
    try:
        return 1.0 / (1.0 + math.exp(-x))
    except OverflowError:
        return 0.0 if x < 0 else 1.0

def sigmoid_derivada(x):
    """Derivada da sigmoide para backpropagation."""
    s = sigmoid(x)
    return s * (1.0 - s)

def relu(x):
    """ReLU — ativação rápida, neurônio liga/desliga."""
    return max(0.0, x)

def relu_derivada(x):
    return 1.0 if x > 0 else 0.0

def tanh(x):
    """Tangente hiperbólica — ativação entre -1 e 1."""
    try:
        return math.tanh(x)
    except OverflowError:
        return 1.0 if x > 0 else -1.0

def tanh_derivada(x):
    t = tanh(x)
    return 1.0 - t * t

def softmax(valores):
    """Softmax — transforma valores em probabilidades."""
    max_val = max(valores)
    exps = [math.exp(v - max_val) for v in valores]
    soma = sum(exps)
    return [e / soma for e in exps]


# ── Classe Neurônio ────────────────────────────────────────────────────

class Neuronio:
    """Um único neurônio artificial."""

    def __init__(self, num_entradas, funcao_ativacao="sigmoid"):
        # Pesos sinápticos aleatórios (inicialização Xavier)
        limite = math.sqrt(6.0 / (num_entradas + 1))
        self.pesos = [random.uniform(-limite, limite) for _ in range(num_entradas)]
        self.bias = random.uniform(-0.1, 0.1)
        self.funcao_ativacao = funcao_ativacao
        
        # Estado interno
        self.ultimo_input = []
        self.ultimo_z = 0.0  # Valor antes da ativação
        self.ultima_saida = 0.0
        self.delta = 0.0  # Gradiente para backprop

    def ativar(self, entradas):
        """Calcula a saída do neurônio."""
        self.ultimo_input = entradas
        self.ultimo_z = sum(w * x for w, x in zip(self.pesos, entradas)) + self.bias
        
        if self.funcao_ativacao == "sigmoid":
            self.ultima_saida = sigmoid(self.ultimo_z)
        elif self.funcao_ativacao == "relu":
            self.ultima_saida = relu(self.ultimo_z)
        elif self.funcao_ativacao == "tanh":
            self.ultima_saida = tanh(self.ultimo_z)
        else:
            self.ultima_saida = self.ultimo_z  # Linear
        
        return self.ultima_saida

    def derivada_ativacao(self):
        """Retorna a derivada da função de ativação."""
        if self.funcao_ativacao == "sigmoid":
            return sigmoid_derivada(self.ultimo_z)
        elif self.funcao_ativacao == "relu":
            return relu_derivada(self.ultimo_z)
        elif self.funcao_ativacao == "tanh":
            return tanh_derivada(self.ultimo_z)
        return 1.0


# ── Classe Camada ──────────────────────────────────────────────────────

class Camada:
    """Uma camada de neurônios (córtex neural)."""

    def __init__(self, num_neuronios, num_entradas, funcao_ativacao="sigmoid"):
        self.neuronios = [
            Neuronio(num_entradas, funcao_ativacao) for _ in range(num_neuronios)
        ]
        self.num_neuronios = num_neuronios

    def propagar(self, entradas):
        """Forward pass — propaga sinal pela camada."""
        return [neuronio.ativar(entradas) for neuronio in self.neuronios]


# ── Classe Rede Neural ────────────────────────────────────────────────

class RedeNeural:
    """
    Rede Neural Feedforward Multicamada — O Cérebro Artificial Faux.
    
    Arquitetura flexível: pode ter qualquer número de camadas e neurônios.
    Usa backpropagation para aprender (como consolidação de memória no sono).
    """

    def __init__(self, arquitetura, funcao_ativacao="sigmoid", taxa_aprendizado=0.1):
        """
        Args:
            arquitetura: lista com número de neurônios por camada.
                         Ex: [4, 8, 4, 2] = 4 entradas, 2 ocultas (8, 4), 2 saídas
            funcao_ativacao: "sigmoid", "relu", "tanh"
            taxa_aprendizado: quão rápido a rede aprende (0.001 a 1.0)
        """
        self.arquitetura = arquitetura
        self.taxa_aprendizado = taxa_aprendizado
        self.camadas = []
        self.historico_erro = []
        self.epocas_treinadas = 0

        # Cria as camadas (menos a de entrada, que é apenas dados)
        for i in range(1, len(arquitetura)):
            camada = Camada(
                num_neuronios=arquitetura[i],
                num_entradas=arquitetura[i - 1],
                funcao_ativacao=funcao_ativacao
            )
            self.camadas.append(camada)

    def predizer(self, entradas):
        """Forward pass completo — processa input e retorna output."""
        saida = list(entradas)
        for camada in self.camadas:
            saida = camada.propagar(saida)
        return saida

    def treinar(self, dados_entrada, dados_saida, epocas=1000, verbose=True):
        """
        Treina a rede usando backpropagation.
        
        Args:
            dados_entrada: lista de listas de inputs
            dados_saida: lista de listas de outputs esperados
            epocas: quantas vezes passa por todos os dados
            verbose: mostra progresso
        """
        for epoca in range(epocas):
            erro_total = 0.0

            for entrada, saida_esperada in zip(dados_entrada, dados_saida):
                # Forward pass
                saida_atual = self.predizer(entrada)

                # Calcula erro da saída
                erros_saida = [
                    (esperado - atual)
                    for esperado, atual in zip(saida_esperada, saida_atual)
                ]
                erro_total += sum(e ** 2 for e in erros_saida)

                # Backpropagation — propaga erro de volta
                self._backpropagate(erros_saida)

                # Atualiza pesos
                self._atualizar_pesos(entrada)

            erro_medio = erro_total / len(dados_entrada)
            self.historico_erro.append(erro_medio)
            self.epocas_treinadas += 1

            if verbose and (epoca + 1) % max(1, epocas // 10) == 0:
                print(f"  Época {epoca + 1}/{epocas} — Erro: {erro_medio:.6f}")

        return self.historico_erro[-1] if self.historico_erro else 0

    def _backpropagate(self, erros_saida):
        """Propaga o erro da saída até a entrada (aprendizado)."""
        # Última camada (saída)
        camada_saida = self.camadas[-1]
        for i, neuronio in enumerate(camada_saida.neuronios):
            neuronio.delta = erros_saida[i] * neuronio.derivada_ativacao()

        # Camadas ocultas (de trás pra frente)
        for idx in range(len(self.camadas) - 2, -1, -1):
            camada_atual = self.camadas[idx]
            camada_seguinte = self.camadas[idx + 1]

            for i, neuronio in enumerate(camada_atual.neuronios):
                erro = sum(
                    n_seg.pesos[i] * n_seg.delta
                    for n_seg in camada_seguinte.neuronios
                )
                neuronio.delta = erro * neuronio.derivada_ativacao()

    def _atualizar_pesos(self, entrada_original):
        """Atualiza os pesos usando gradiente descendente."""
        for idx, camada in enumerate(self.camadas):
            if idx == 0:
                entradas = entrada_original
            else:
                entradas = [n.ultima_saida for n in self.camadas[idx - 1].neuronios]

            for neuronio in camada.neuronios:
                for j in range(len(neuronio.pesos)):
                    neuronio.pesos[j] += (
                        self.taxa_aprendizado * neuronio.delta * entradas[j]
                    )
                neuronio.bias += self.taxa_aprendizado * neuronio.delta

    # ── Persistência (salvar/carregar o cérebro) ───────────────────────

    def salvar(self, caminho="rede_neural_faux.json"):
        """Salva o estado da rede neural em arquivo JSON."""
        estado = {
            "arquitetura": self.arquitetura,
            "taxa_aprendizado": self.taxa_aprendizado,
            "epocas_treinadas": self.epocas_treinadas,
            "camadas": []
        }
        for camada in self.camadas:
            neuronios_data = []
            for n in camada.neuronios:
                neuronios_data.append({
                    "pesos": n.pesos,
                    "bias": n.bias,
                    "funcao_ativacao": n.funcao_ativacao
                })
            estado["camadas"].append(neuronios_data)
        
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(estado, f, indent=2, ensure_ascii=False)
        print(f"💾 Rede neural salva em: {caminho}")

    @classmethod
    def carregar(cls, caminho="rede_neural_faux.json"):
        """Carrega uma rede neural de arquivo JSON."""
        if not os.path.exists(caminho):
            return None
        
        with open(caminho, 'r', encoding='utf-8') as f:
            estado = json.load(f)
        
        rede = cls(estado["arquitetura"], taxa_aprendizado=estado["taxa_aprendizado"])
        rede.epocas_treinadas = estado["epocas_treinadas"]
        
        for i, camada_data in enumerate(estado["camadas"]):
            for j, n_data in enumerate(camada_data):
                rede.camadas[i].neuronios[j].pesos = n_data["pesos"]
                rede.camadas[i].neuronios[j].bias = n_data["bias"]
                rede.camadas[i].neuronios[j].funcao_ativacao = n_data["funcao_ativacao"]
        
        print(f"🧠 Rede neural carregada! ({rede.epocas_treinadas} épocas treinadas)")
        return rede

    def info(self):
        """Retorna informações sobre a rede."""
        total_pesos = sum(
            len(n.pesos) + 1  # +1 pro bias
            for c in self.camadas
            for n in c.neuronios
        )
        return {
            "arquitetura": self.arquitetura,
            "total_camadas": len(self.camadas),
            "total_neuronios": sum(c.num_neuronios for c in self.camadas),
            "total_parametros": total_pesos,
            "epocas_treinadas": self.epocas_treinadas,
            "ultimo_erro": self.historico_erro[-1] if self.historico_erro else None
        }


# ── Teste Rápido ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Testando Rede Neural Faux")
    print("=" * 50)

    # Teste clássico: aprender XOR (problema não-linear)
    print("\n📡 Treinando para aprender XOR...")
    rede = RedeNeural([2, 4, 1], funcao_ativacao="sigmoid", taxa_aprendizado=0.5)

    entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [[0], [1], [1], [0]]

    rede.treinar(entradas, saidas, epocas=5000, verbose=True)

    print("\n📊 Resultados:")
    for e, s in zip(entradas, saidas):
        pred = rede.predizer(e)
        print(f"  Input: {e} → Predição: {pred[0]:.4f} (Esperado: {s[0]})")

    print(f"\n📈 Info: {rede.info()}")
    rede.salvar()
