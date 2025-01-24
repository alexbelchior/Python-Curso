palavra = 'Python'

print(palavra.upper()) # 'PYTHON'
print('---------------------------------------------')
print(palavra.lower()) # 'python'
print('---------------------------------------------')
print(palavra.capitalize()) # 'Python'
print('---------------------------------------------')


# Verificar se uma string termina com determinado caractere

palavra = '2025_01_14_NotaFiscal.pdf'

print(f'A palavra {palavra} termina com .pdf?')
print(palavra.endswith('.pdf')) # True
print('---------------------------------------------')

# Verificar se uma string começa com determinado caractere
print(f'A palavra {palavra} começa com 2025?')
print(palavra.startswith('2025')) # True
print('---------------------------------------------')

# Verificar quantas vezes um caractere aparece em uma string
frase = 'Python é uma linguagem de programação muito poderosa'
resultado = frase.count('a') # 6
print(f'A letra "a" aparece {resultado} vezes na frase "{frase}"')
print('---------------------------------------------')

# Encontrar a posição de um caractere em uma string
palavra = 'aaabaacbaaaabadaf'
print(palavra.find('b')) # 3
print(palavra.index('b')) # 3

# Se o caractere não existir, o método find() retorna -1
print(palavra.find('z')) # -1
print('---------------------------------------------')

# Para pegar uma string a partir de uma determinada posição
print(palavra[palavra.find('b'):]) # Pega a palavra a partir da posição b em diante
print('---------------------------------------------')

# Para checar se uma string é composta apenas por números
numero = '123456'
print(f'A varíavel {numero} contém apenas números? {numero.isdigit()}') # True

# Para checar se uma string é composta apenas por letras
letras = 'Python'
print(f'A varíavel {letras} é alpha? {letras.isalpha()}') # True
print('---------------------------------------------')

# Para trocar um caractere por outro
frase = 'Python é uma linguagem de programação muito poderosa'
print(f'Vamos trocar na frase "{frase}" Python por Java => {frase.replace('Python', 'Java')}') # Substitui Python por Java
print('---------------------------------------------')

# Para remover espaços em branco no início e no final de uma string
frase = '    Python é uma linguagem de programação muito poderosa    '
print(frase.strip())
print('---------------------------------------------')

# Para remover espaços em branco no início de uma string
frase = '    Python é uma linguagem de programação muito poderosa    '
print(frase.lstrip())
print('---------------------------------------------')

# Para remover espaços em branco no final de uma string
frase = '    Python é uma linguagem de programação muito poderosa    '
print(frase.rstrip())
print('---------------------------------------------')

# Para dividir uma string em uma lista
frase = 'Python é uma linguagem de programação muito poderosa'
print(frase.split()) # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'muito', 'poderosa']

# Para dividir uma string em uma lista, passando um caractere específico
frase = 'Python, é, uma, linguagem, de, programação, muito, poderosa'
print(frase.split(',')) # ['Python', ' é', ' uma', ' linguagem', ' de', ' programação', ' muito', ' poderosa']

# Para juntar uma lista em uma string
lista = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'muito', 'poderosa']
print(' '.join(lista)) # 'Python é uma linguagem de programação muito poderosa'

# Para juntar uma lista em uma string, passando um caractere específico
lista = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'muito', 'poderosa']
print(' - '.join(lista)) # 'Python - é - uma - linguagem - de - programação - muito - poderosa'
print('---------------------------------------------')

# Para inverter uma string
frase = 'Python é uma linguagem de programação muito poderosa'
print(frase[::-1]) # 'asoredep otium oãçamgail amu é nohtyP'
print('---------------------------------------------')

# Para verificar se uma string é composta apenas por letras minúsculas
frase = 'python'
print(f'A frase "{frase}" é composta apenas por letras minúsculas? {frase.islower()}') # True
print('---------------------------------------------')

# Para verificar se uma string é composta apenas por letras maiúsculas
frase = 'PYTHON'
print(f'A frase "{frase}" é composta apenas por letras maiúsculas? {frase.isupper()}') # True
print('---------------------------------------------')

# Para transformar uma string em uma lista
frase = 'Python é uma linguagem de programação muito poderosa'
print(frase.split()) # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'muito', 'poderosa']
print('---------------------------------------------')

# Para transformar uma lista em uma string usando um cararter específico como separador
frase = 'Item 1 - Item 2 - Item 3 - Item 4 - Item 5'
lista = frase.split(' - ')
print(lista) # ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
print('---------------------------------------------')

