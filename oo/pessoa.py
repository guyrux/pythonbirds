class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
    
    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == "__main__":
    p = Pessoa("Gustavo")
    print(p.nome)
    print(id(p))
    print(p.cumprimentar())
    p.nome = "Suto"
    print(p.nome)