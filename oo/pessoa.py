class Pessoa:
    # Atributo de classe. Deve ser usado quando todas as instâncias tiverem o mesmo valor.
    olhos = 2
    ser = "Pessoa"

    # Atributos de dado ou apenas atributos
    def __init__(self, *filhos, nome=None, idade=35): 
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    
    # Método
    def cumprimentar(self):
        return f"Olá {id(self)}"

    # Método de classe: Método que independe do objeto que está sendo executado
    # Pode-se fazer isso usando decorators
    @staticmethod
    def metodo_estatico():
        return "método estático"

    # Método de classe com decorator @classmethod.
    # Com esse é possível acessar a classe que está executando esse método.
    # No caso, o parâmetro cls representa a palavra class; porém, como class é uma palavra reservada, usamos o cls.
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

if __name__ == "__main__":
    gustavo = Mutante(nome="Gustavo")
    jose = Pessoa(gustavo, nome="José", idade=66)
    print(jose.nome)
    print(id(jose))
    print(jose.cumprimentar())
    for filho in jose.filhos:
        print(f"Um dos filhos de {jose.nome} chama {filho.nome}.")
    gustavo.olhos = 1

    # Criando um atributo dinâmico
    gustavo.sobrenome = "Suto"

    # Acessando todos os atributos de um objeto, mesmo os atributos dinâmicos.
    print(gustavo.__dict__)
    print(jose.__dict__)

    print(f"{gustavo.nome} tem {gustavo.olhos} olhos.")
    print(f"Pessoa tem {Pessoa.olhos} olhos.")

    # Usando o método de classe sob o decorator @staticmethod:
    print(f"{Pessoa.ser}: {Pessoa.metodo_estatico()}, {gustavo.nome}: {gustavo.metodo_estatico()}")

    # Usando o método de classe sob o decorator @classmethod:
    print(f"""{Pessoa.ser}: {Pessoa.nome_e_atributos_de_classe()}
{gustavo.nome}: {gustavo.nome_e_atributos_de_classe()}""")