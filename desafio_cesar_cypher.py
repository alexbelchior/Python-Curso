# Crie um código que implementa a "Cifra de César", isto é, que
# transforma uma string movendo cada letra um certo número de
# posições no alfabeto. O número de passo é dado por uma chave.
# Letra com aceitos, espaços e pontuação permanecem iguais.

# Exemplos
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# Cachorro com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# Dica: construa duas strings com as letras do alfabeto em ordem,
# um para letras minúsculas e outro para letras maiúsculas.
# E use essa string para guiar as substituições.

alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifra_cesar(texto, chave):
    texto_cifrado = ''
    for letra in texto:
        if letra in alfabeto_minusculo:
            indice = alfabeto_minusculo.index(letra)
            indice = (indice + chave) % 26 # 26 é o tamanho do alfabeto
            texto_cifrado += alfabeto_minusculo[indice]
        elif letra in alfabeto_maiusculo:
            indice = alfabeto_maiusculo.index(letra)
            indice = (indice + chave) % 26
            texto_cifrado += alfabeto_maiusculo[indice]
        else:
            texto_cifrado += letra

        if len(texto_cifrado) == len(texto):
            return texto_cifrado

        
texto = "Alexandre"
chave = 3
texto_cifrado = cifra_cesar(texto, chave)
print(texto_cifrado) # Dohahugrh