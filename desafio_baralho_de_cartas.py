import random

def gerar_baralho(numero_copias = 2, coringas = False, embaralhado = True):
    naipes = ['♠', '♦', '♣', '♥']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = [
        (valor, naipe) 
        for _ in range(numero_copias) 
            for naipe in naipes 
                for valor in valores]
    if coringas:
        baralho.append(('Coringa', ''))
        baralho.append(('Coringa', ''))
    if embaralhado:
        random.shuffle(baralho)
    return baralho

def mostrar_cartas(cartas):
    for carta in cartas:
        print(f'{carta[0]}{carta[1]}', end=' ') # Exibe a carta
    print()

def jogar_baralho():
    baralho = gerar_baralho()
    cartas_jogador = baralho[:5] # 5 primeiras cartas
    cartas_mesa = baralho[5:10] # 5 cartas seguintes
    mostrar_cartas(cartas_jogador) # Mostra as cartas do jogador
    mostrar_cartas(cartas_mesa) # Mostra as cartas da mesa

jogar_baralho()