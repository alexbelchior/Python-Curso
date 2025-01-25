# Crie um jogo dos estados. Neste jogo, o jogador precisa responder
# corretamente qual é a capital de cada estado do Brasil.
# O jogo deve perguntar de forma aleatória "Qual é a capital do estado X?" e checar se
# o jogador acertou. A pergunta não deve ser repetir, ou seja, se o jogo perguntar sobre uma capital
# e o jogador acertar a resposta essa pergunta não deverá se repetir, apenas em caso do jogador errar,
# nesse caso o jogo deverá perguntar outra capital aleatoriamente que ainda não tenha sido perguntada.
# Após cada pergunta, o jogador pode escolher entre
# continuar jogando ou sair do jogo. Caso o jogador decida sair ou quando
# todas as perguntas forem respondidas, o jogo deve exibir a porcentagem de acertos.

estados = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

import random

acertos = 0
erros = 0
perguntas = list(estados.keys())
while perguntas:
    estado_selecionado = random.choice(perguntas)
    capital = input(f"Qual é a capital do estado {estado_selecionado}? ")
    if capital.lower() == estados[estado_selecionado].lower():
        acertos += 1
        perguntas.remove(estado_selecionado)
    else:
        erros += 1
    continuar = input("Deseja continuar jogando? (s/n) ")
    if continuar.lower() == 'n':
        break

total = acertos + erros
porcentagem_acertos = acertos / total * 100
print(f"Você acertou {acertos} perguntas e errou {erros}.")
print(f"Porcentagem de acertos: {porcentagem_acertos:.2f}%")

