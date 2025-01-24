# Crie um código que conta o número de vogais de um bloco de texto
# qualquer. O código deve desconsiderar letras maiúsculas e minúsculas,
# ou seja, "a" e "A" contam da mesma forma.

# Una forma de colocar uma string com várias linhas é utilizando aspas triplas
texto = """
Python é uma linguagem de programação de alto nível,[10] interpretada 
de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de 
desenvolvimento comunitário, aberto e gerenciado pela organização sem fins 
lucrativos Python Software Foundation. Apesar de várias partes da linguagem 
possuírem padrões e especificações formais, a linguagem, como um todo, 
não é formalmente especificada. O padrão na pratica é a implementação CPython. 
"""
vogais = {
    "A": 0,
    "E": 0,
    "I": 0,
    "O": 0,
    "U": 0
}

for letra in texto:
    if letra.upper() == 'A':
        vogais['A'] += 1
    if letra.upper() == 'E':
        vogais['E'] += 1
    if letra.upper() == 'I':
        vogais['I'] += 1
    if letra.upper() == 'O':
        vogais['O'] += 1
    if letra.upper() == 'U':
        vogais['U'] += 1

for vogal, quantidade in vogais.items():
    print(f'{vogal}: {quantidade}')