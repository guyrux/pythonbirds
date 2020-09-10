"""
Você deve criar uma classe carro que vai possuir
butos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

        N
    O       L
        S

IMPORTANTE:
Para rodar o doctest, no terminal:
python -m doctest <nome_do_arquivo>.py      # rodar todos os testes de uma só vez.
python -m doctest -f <nome_do_arquivo>.py   # rodar testes e para na primeira falha.

>>> # Testando motor
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
>>> # Testando Direcao
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
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
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

"""

class Direcao:

    def __init__(self, valor="Norte"):
        self.valor = valor
    
    def girar_a_direita(self):
        if self.valor == "Norte":
            self.valor = "Leste"
        elif self.valor == "Leste":
            self.valor = "Sul"
        elif self.valor == "Sul":
            self.valor = "Oeste"
        else:
            self.valor = "Norte"
    
    def girar_a_esquerda(self):
        if self.valor == "Norte":
            self.valor = "Oeste"
        elif self.valor == "Oeste":
            self.valor = "Sul"
        elif self.valor == "Sul":
            self.valor = "Leste"
        else:
            self.valor = "Norte"


class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
            
    def frear(self):
        if self.velocidade-2 < 0:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Carro:
    ## Se eu tivesse deixado as classes Motor e Direcao em arquivos separados do
    ## carro.py, as chamadas de impoortação deveriam ser colocadas.
    # from direcao import Direcao
    # from motor import Motor

    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor
    
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


# if __name__ == "__main__":
#     from direcao import Direcao
#     from motor import Motor
#     carro = Carro(Direcao("Sul"), Motor(10))
#     print(carro.calcular_velocidade())
#     print(0)
#     carro.acelerar()
#     print(carro.calcular_velocidade())
#     print(1)
#     carro.acelerar()
#     print(carro.calcular_velocidade())
#     print(2)
#     carro.frear()
#     print(carro.calcular_velocidade())
#     print(0)
#     print(carro.calcular_direcao())
#     print('Norte')
#     carro.girar_a_direita()
#     print(carro.calcular_direcao())
#     print('Leste')
#     carro.girar_a_esquerda()
#     print(carro.calcular_direcao())
#     print('Norte')
#     carro.girar_a_esquerda()
#     print(carro.calcular_direcao())
#     print('Oeste')
