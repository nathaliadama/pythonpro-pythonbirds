class Pessoa:

    # Atributos de dados (data attributes)
    def __init__(self, nome=None, idade=35, *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


# Testes
if __name__ == '__main__':
    p = Pessoa()

    # Formas de acessar o método.
    print(p.cumprimentar())  # Passando p de forma implícita.
    print(Pessoa.cumprimentar(p))
    print(id(p))

    # Acessando atributos
    print(p.nome)

    # Alterando diretamente o atributo
    p.nome = "Ronald"
    print(p.nome)

    # Utilizando o parâmetro passado...
    p1 = Pessoa("Ronald")
    print(p1.nome)

    # Utilizando o parâmetro passado...
    p2 = Pessoa("Ronald", 39)
    print(p2.nome + " tem " + str(p2.idade))

    # Utilizando o parâmetro passado...
    p3 = Pessoa("Ronald", 39, 'Olga', 'Enzo', 'Mel')
    print(p3.nome + " tem " + str(p3.idade))
    print("filhos: ")
    for filho in p3.filhos:
        print(filho)

    # Atribuição dinâmica de atributos
    p3.sobrenome = "B. Falcão"
    print(p3.sobrenome)

    # A linha abaixo se executada apresenta erro.
    # print(p2.sobrenome)
