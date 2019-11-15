class Pessoa:
    def __init__(self, *filhos, nome="Gustavo", idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, {self.nome}!"

if __name__ == '__main__':
    filho01 = Pessoa(nome="Gu", idade=34)
    filho02 = Pessoa(nome="Gui", idade=32)
    pai = Pessoa(filho01, filho02, nome="José", idade=64)
    print(pai.cumprimentar())
    print(f"{pai.nome} tem {pai.idade} anos e {len(pai.filhos)} filhos.")

    for i, filho in enumerate(pai.filhos):
        print(f"O {i+1}º chama {filho.nome}.")

    pai.sobrenome = "Souza"
    print(pai.nome, pai.__dict__)
    print(filho01.nome, filho01.__dict__)

