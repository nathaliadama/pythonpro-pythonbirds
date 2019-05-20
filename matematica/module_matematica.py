def multiplica(fator_a, fator_b):
    """Função para multiplicação de dois fatores passados"""
    return fator_a * fator_b


"""
__<method>__ is dunder or magic methods
"""
print(__name__)  # Retorna o nome do módulo.


"""
Forma simples de fazer um teste do módulo!
O teste não será executado fora do módulo.
"""
if __name__ == '__main__':
    print(f'Teste do módulo {__name__}.')
