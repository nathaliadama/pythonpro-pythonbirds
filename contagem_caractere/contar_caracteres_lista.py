"""
Módulo que executa a contagem de caracteres e retorna uma lista.
"""


def contar_caracteres_sorted(palavra):
    """ Função para a contagem de caracteres usando a abordagem do sorted().
    Exemplo:
    >>> contar_caracteres_sorted('ronald')
    {'a': 1, 'd': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1}
    >>> contar_caracteres_sorted('ana')
    {'a': 2, 'n': 1}

    :param palavra: String

    """
    caracteres_ordenados = sorted(palavra)

    caracter_anterior = caracteres_ordenados[0]

    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1

    resultado[caracter_anterior] = contagem  # Apresentando o último caracter

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
