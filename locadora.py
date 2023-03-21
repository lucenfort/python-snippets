import os

carros = [
    ("Volkswagen Fusca", 80),
    ("Volkswagen Gol", 120),
    ("Fiat Uno", 100),
    ("Fiat Palio", 110),
    ("Chevrolet Celta", 90),
    ("Chevrolet Corsa", 95),
    ("Volkswagen Fox", 130),
    ("Chevrolet Onix", 150),
    ("Ford Ka", 110),
    ("Ford Fiesta", 120),
    ("Fiat Siena", 130),
    ("Renault Sandero", 140),
    ("Renault Logan", 145),
    ("Honda Civic", 200),
    ("Toyota Corolla", 220),
    ("Toyota Etios", 130),
    ("Hyundai HB20", 150),
    ("Hyundai Creta", 250),
    ("Hyundai Tucson", 280),
    ("Jeep Renegade", 200),
    ("Nissan Versa", 120),
    ("Nissan Sentra", 150),
    ("Chevrolet Cruze", 180),
    ("Chevrolet Spin", 160),
    ("Fiat Toro", 230),
    ("Fiat Strada", 150),
    ("Ford Ranger", 300),
    ("Ford EcoSport", 140),
    ("Renault Duster", 160),
    ("Renault Captur", 180),
    ("Peugeot 2008", 170),
    ("Peugeot 208", 140),
    ("Honda Fit", 150),
    ("Honda WR-V", 170),
    ("Toyota Yaris", 140),
    ("Toyota Hilux", 350),
    ("Volkswagen Amarok", 300),
    ("Volkswagen Saveiro", 130),
    ("Mitsubishi L200", 320),
    ("Mitsubishi Outlander", 220),
    ("Chevrolet Tracker", 180),
    ("Chevrolet S10", 300),
    ("Ford Edge", 280),
    ("Ford Fusion", 220),
    ("Jeep Compass", 200),
    ("Jeep Grand Cherokee", 400),
    ("Hyundai Santa Fe", 280),
    ("Hyundai ix35", 200),
    ("Renault Kwid", 100)
]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {}/dia.".format(i, car[0], car[1]))

#mostrar_lista_de_carros(carros)

while True:
    os.system("cls")
    print("================================")
    print("Bem vindo a locadora de carros!")
    print("================================")

    print("\nEscolha uma opção:")
    print("0 - Mostrar portifólio | 1 - Alugar carro | 2 - Devolver carro")

    op = int(input())

    os.system("cls")    

    if op == 0:
        mostrar_lista_de_carros(carros)
    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("\n================================")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("cls")

        print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod_car][1]))
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0: 
            print("Não há carros para devolver")
        else:
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print("")
    print("================================")
    print("0 para CONTINUAR | 1 para SAIR")
    comando = int(input())
    if comando == 1:
        break
