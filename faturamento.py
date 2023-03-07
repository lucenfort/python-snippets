import json

def ler_arquivo_json(caminho_arquivo: str) -> list:
    """Lê um arquivo JSON e retorna uma lista com os valores de faturamento.

    Args:
        caminho_arquivo (str): O caminho para o arquivo JSON.

    Returns:
        list: Uma lista com os valores de faturamento diário.
    """
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados['faturamento']

def calcular_faturamento(dados: list) -> tuple:
    """Calcula o menor e o maior valor de faturamento diário e o número de dias
    em que o faturamento diário foi superior à média mensal.

    Args:
        dados (list): Uma lista com os valores de faturamento diário.

    Returns:
        tuple: Uma tupla contendo o menor e o maior valor de faturamento diário
               e o número de dias em que o faturamento diário foi superior à média mensal.
    """
    soma = 0
    num_dias = 0
    for faturamento in dados:
        soma += faturamento
        num_dias += 1 if faturamento > soma/len(dados) else 0
    return min(dados), max(dados), num_dias

# Exemplo:  
dados = ler_arquivo_json('faturamento.json')
menor, maior, num_dias_superior_media = calcular_faturamento(dados)
print(f"Menor valor de faturamento diário: R${menor:.2f}")
print(f"Maior valor de faturamento diário: R${maior:.2f}")
print(f"Número de dias em que o faturamento diário foi superior à média mensal: {num_dias_superior_media}")
