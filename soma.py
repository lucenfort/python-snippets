
def somar_ate(n: int) -> int:
    """Calcula a soma de todos os números inteiros de 1 a n.

    Args:
        n (int): O valor limite para a soma.

    Returns:
        int: A soma de todos os números inteiros de 1 a n.
    """
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

# Exemplo:
print(somar_ate(100))
