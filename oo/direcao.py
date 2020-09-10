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


if __name__ == "__main__":
    # Testando Direcao
    direcao = Direcao()
    print(direcao.valor)
    print('Norte')
    direcao.girar_a_direita()
    print(direcao.valor)
    print('Leste')
    direcao.girar_a_direita()
    print(direcao.valor)
    print('Sul')
    direcao.girar_a_direita()
    print(direcao.valor)
    print('Oeste')
    direcao.girar_a_direita()
    print(direcao.valor)
    print('Norte')
    direcao.girar_a_esquerda()
    print(direcao.valor)
    print('Oeste')
    direcao.girar_a_esquerda()
    print(direcao.valor)
    print('Sul')
    direcao.girar_a_esquerda()
    print(direcao.valor)
    print('Leste')
    direcao.girar_a_esquerda()
    print(direcao.valor)
    print('Norte')

