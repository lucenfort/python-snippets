def fibonacci(num: int) -> bool:
    """Verifica se um número pertence à sequência de Fibonacci.

    Args:
        num (int): O número a ser verificado.

    Returns:
        bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

# Exemplo
num = int(input("Digite um número: "))
if fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
