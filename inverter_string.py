def inverter_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

texto = "Exemplo de string a ser invertida"
texto_invertido = inverter_string(texto)
print(texto_invertido)
