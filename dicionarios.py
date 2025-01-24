capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Peru': 'Lima',
    'Colômbia': 'Bogotá',
    'Uruguai': 'Montevidéu',
    'Paraguai': 'Assunção',
    'Venezuela': 'Caracas',
    'Equador': 'Quito',
    'Bolívia': 'La Paz',
    'Guiana': 'Georgetown',
    'Suriname': 'Paramaribo',
    'Guiana Francesa': 'Caiena' ,
    'Portugal': 'Lisboa',
    'Espanha': 'Madri',
    'França': 'Paris',
    'Itália':'Roma',
    'Alemanha': 'Berlim',
    'Reino Unido': 'Londres',
    'Holanda': 'Amsterdã',
    'Bélgica': 'Bruxelas',
    'Luxemburgo': 'Luxemburgo',
    'Suíça': 'Berna'
}

print(capitais)
print(capitais['Bélgica'])
print('---------------------------------------------')
# Para adicionar um novo item ao dicionário, basta fazer:
capitais['Noruega'] = 'Oslo'

print(capitais)
print('---------------------------------------------')
print(capitais['Noruega'])
print('---------------------------------------------')
# Para remover um item do dicionário, basta fazer:
del capitais['Noruega']
print(capitais)
#print(capitais['Noruega']) # Erro, pois o item foi removido
print('---------------------------------------------')
pais = 'Noruega'
if pais in capitais:
    print(f'A capital do(a) {pais} é {capitais[pais]}')
else:
    print(f'{pais} não está no dicionário de capitais')
print('---------------------------------------------')

# Um dicionário não apresenta em ordem os itens, são exibidos conforme a ordem de inserção
for pais in capitais:
    print(f'A capital do(a) {pais} é {capitais[pais]}')

print('---------------------------------------------')

# Para verificar se uma chave existe dentro do dicionário, basta fazer:
print('Brasil' in capitais) # True
print('Noruega' in capitais) # False
valor_existe = 'Brasil' in capitais
print(f'Brasil existe no dicionário de capitais: {valor_existe}') # True
print('---------------------------------------------')


produtos ={
    'banana': 2.50,
    'maçã': 3.50,
    'laranja': 4.00,
    'uva': 5.00,
    'melancia': 10.00
}

print(produtos.get('laranja')) # 4.0

# Se o item não existir, o método get() retorna None
# Uma outra forma de evitar erro é passar um valor padrão para o método get()
print(produtos.get('pera', 'Produto não encontrado')) # Produto não encontrado
print('---------------------------------------------')

# Abaixo algumas formas de percorrer um dicionário

# 1ª forma - Retorna as chaves
for produto in produtos:
    print(produto)

print('---------------------------------------------')

# 2ª forma - Retorna as chaves
for produto in produtos.keys():
    print(produto)

print('---------------------------------------------')

# 3ª forma - Retorna os valores das chaves
for valor in produtos.values():
    print(valor)

print('---------------------------------------------')

# 4ª forma - Retorna as chaves e os valores
for item in produtos.items():
    print(item)

print('---------------------------------------------')

# 5ª forma - Retorna as chaves e os valores
for chave, valor in produtos.items():
    print(f'{chave} - R$ {valor:.2f}')

print('---------------------------------------------')

# Atualizando um dicionário com outro dicionário
produtos2 = {
    'pera': 2.00,
    'abacaxi': 5.00,
    'melão': 8.00
}

produtos.update(produtos2)

for chave, valor in produtos.items():
    print(f'{chave} - R$ {valor:.2f}')	

print('---------------------------------------------')

# Para copiar um dicionário para outro, basta fazer:
produtos3 = produtos.copy()
produtos3['morango'] = 6.00 # Adicionando um novo item ao dicionário produtos3

print(f'Produtos: {produtos}')
print(f'Produtos3: {produtos3}')

print('---------------------------------------------')