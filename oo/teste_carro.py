from unittest import TestCase

from oo.carro import Motor
from oo.carro import Direcao
from oo.carro import Carro

class CarroTestCase(TestCase):
    def teste_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_aceleracao(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)
    
    def teste_frenagem(self):
        motor = Motor(3)
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def teste_direcao(self):
        direcao = Direcao()
        self.assertEqual("Norte", direcao.valor)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual("Leste", direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual("Sul", direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual("Oeste", direcao.valor)

    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual("Oeste", direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual("Sul", direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual("Leste", direcao.valor)

    def teste_carro(self):
        carro = Carro()
        self.assertEqual(0, carro.calcular_velocidade())



# >>> carro = Carro(direcao, motor)
# >>> carro.calcular_velocidade()
# 0
# >>> carro.acelerar()
# >>> carro.calcular_velocidade()
# 1
# >>> carro.acelerar()
# >>> carro.calcular_velocidade()
# 2
# >>> carro.frear()
# >>> carro.calcular_velocidade()
# 0
# >>> carro.calcular_direcao()
# 'Norte'
# >>> carro.girar_a_direita()
# >>> carro.calcular_direcao()
# 'Leste'
# >>> carro.girar_a_esquerda()
# >>> carro.calcular_direcao()
# 'Norte'
# >>> carro.girar_a_esquerda()
# >>> carro.calcular_direcao()
# 'Oeste'