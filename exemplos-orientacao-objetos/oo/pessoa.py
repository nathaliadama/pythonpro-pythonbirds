class Pessoa:

    olhos = 2  # Atributo Default ou Atributo de Classe.

    # Atributos de dados (data attributes)
    def __init__(self, nome=None, idade=35, *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 11 + 31

    @classmethod
    def nomes_atributos_classe(cls):
        """Usado para acessar dados da própria classe"""
        return f'{cls} - olhos - {cls.olhos}'


class Homem(Pessoa):
    pass


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

    # Criação dinâmica de atributos
    p3.sobrenome = "B. Falcão"
    print(p3.sobrenome)

    # A linha abaixo se executada apresenta erro.
    # print(p2.sobrenome)

    # Verificando os objetos criados.
    print(p2.__dict__)  # Aqui NÃO temos o atributo criado dinamicamente.
    print(p3.__dict__)  # Aqui TEMOS o atributo criado dinamicamente.

    # Removendo atributos de forma dinâmica
    del p2.filhos

    print("Objeto após a deleção de um atributo:")

    # Verificando os objetos após a deleção.
    print(p2.__dict__)  # Aqui NÃO temos o atributo criado dinamicamente.
    print(p3.__dict__)  # Aqui TEMOS o atributo criado dinamicamente.

    # Acessando atributos de classe.
    print(f'Número de olhos em Pessoa: {Pessoa.olhos}')
    print(f'Número de olhos em P1: {p1.olhos}')
    print(f'Número de olhos em P2: {p2.olhos}')
    print(f'Número de olhos em P3: {p3.olhos}')

    # Exemplo de como estão os dicionários dos objetos.
    print(p3.__dict__)  # Nesse momento o atributo ainda não faz parte do dict.

    # Alterando um atributo de classe de um objeto
    p3.olhos = 3

    # Mostrando o resultado da alteração.
    print("\nResultado após a alteração")
    print(f'Número de olhos em Pessoa: {Pessoa.olhos}')
    print(f'Número de olhos em P3: {p3.olhos}')

    # Verificando os dicionários após a alteração.
    print(p3.__dict__)

    # Vamos verificar como os objetos foram alterados.
    print(f'ID Objeto Pessoa: {id(Pessoa.olhos)}')
    print(f'ID Objeto p1: {id(p1.olhos)}')  # Compartilha o atributo
    print(f'ID Objeto p2: {id(p2.olhos)}')  # Compartilha o atributo
    print(f'ID Objeto p3: {id(p3.olhos)}')  # Criado novo espaço na memória.

    # Fazendo a alteração no atributo default na própria classe.
    Pessoa.olhos = 4
    print(f'ID Objeto Pessoa: {Pessoa.olhos}')
    print(f'ID Objeto p1: {p1.olhos}')  # Compartilha o atributo
    print(f'ID Objeto p2: {p2.olhos}')  # Compartilha o atributo
    print(f'ID Objeto p3: {p3.olhos}')  # Criado novo espaço na memória.

    # Apagando o valor alterado em p3 e verificando o resultado.
    del p3.olhos
    print(f'ID Objeto Pessoa: {Pessoa.olhos}')
    print(f'ID Objeto p1: {p1.olhos}')  # Compartilha o atributo
    print(f'ID Objeto p2: {p2.olhos}')  # Compartilha o atributo
    print(f'ID Objeto p3: {p3.olhos}')  # Criado novo espaço na memória.

    # Verificando o dict de p3
    print(p3.__dict__)

    # Executando os métodos estáticos.
    print(Pessoa.metodo_estatico())  # Diretamente pela classe.
    print(p1.metodo_estatico())  # Ou pelo objeto.

    # Acessando os métodos de classe
    print(Pessoa.nomes_atributos_classe())  # Acessando pela classe.
    print(p1.nomes_atributos_classe())  # Acessando pelo objeto.

    # Testando a classe herdada de Pessoa
    homem = Homem("Ronald", 39)
    print(homem.nome)
    print(homem.idade)

    # Verificando a instância da classe
    print(isinstance(p1, Pessoa))
    print(isinstance(homem, Pessoa))
    print(isinstance(homem, Homem))
