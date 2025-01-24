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