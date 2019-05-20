"""
Módulo que executa a contagem de caracteres e retorna uma lista, com uma
melhoria no código.
"""


def contar_caracteres_sorted(palavra):
    """ Função para a contagem de caracteres usando a abordagem do sorted().
    Exemplo:
    >>> contar_caracteres_sorted('ronald')
    {'r': 1, 'o': 1, 'n': 1, 'a': 1, 'l': 1, 'd': 1}
    >>> contar_caracteres_sorted('ana')
    {'a': 2, 'n': 1}

    :param palavra: String

    """

    resultado = {}

    for caracter in palavra:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


# Primeiro exemplo do HELP...
if __name__ == '__main__':
    print('-' * 10)
    print(contar_caracteres_sorted("ronald"))

# Segundo exemplo do HELP...
if __name__ == '__main__':
    print('-' * 10)
    print(contar_caracteres_sorted("ana"))

# Outros exemplos de teste.
if __name__ == '__main__':
    print('-' * 10)
    print(contar_caracteres_sorted("banana"))
    print('-' * 10)
    print(contar_caracteres_sorted("fabric"))
