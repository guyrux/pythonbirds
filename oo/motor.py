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

        

if __name__ == "__main__":
    motor = Motor()
    motor.velocidade
    print(motor.velocidade)
    print(0)
    motor.acelerar()
    motor.velocidade
    print(motor.velocidade)
    print(1)
    motor.acelerar()
    motor.velocidade
    print(motor.velocidade)
    print(2)
    motor.acelerar()
    motor.velocidade
    print(motor.velocidade)
    print(3)
    motor.frear()
    motor.velocidade
    print(motor.velocidade)
    print(1)
    motor.frear()
    motor.velocidade
    print(motor.velocidade)
    print(0)
