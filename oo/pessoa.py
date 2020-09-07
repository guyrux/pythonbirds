class Pessoa:
    def __init__(self, *filhos,nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == "__main__":
    gustavo = Pessoa(nome="Gustavo")
    jose = Pessoa(gustavo, nome="José", idade=66)
    print(jose.nome)
    print(id(jose))
    print(jose.cumprimentar())
    for filho in jose.filhos:
        print(f"Um dos filhos de {jose.nome} chama {filho.nome}.")

    gustavo.sobrenome = "Suto"  # Criando um atributo dinâmico
    print(gustavo.__dict__)     # Acessando todos os atributos de um objeto, mesmo os atributos dinâmicos.
    print(jose.__dict__)
