"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade. Ele oferecerá os seguintes atributos:
a) Atributo de dado Velocidade.
b) Método acelerar, que deverá incrementar a velocidade em uma unidade.
c) Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
a) Valor da direção com valores possíveis: norte, sul, leste e oeste.
b) Método girar a direita (N -> L -> S -> O -> N)
b) Método girar a esquerda (N -> O -> S -> L -> N)

Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.gerar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.gerar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.gerar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.gerar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.gerar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.gerar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.gerar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
"""

# Definindo constantes.
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        pass

    def girar_a_esquerda(self):
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE
