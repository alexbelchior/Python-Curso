print("Ola mundo")

idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

print('------INICIO------')

resposta1 = input('Estou com fome? (Digite s para SIM e n para NÃO): ')
if resposta1 == 's':
    resposta2 = input('Tenho comida? (Digite s para SIM e n para NÃO): ')
    if resposta2 != 's':
        print('Ir ao mercado')
        print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')
print(f'------FIM------\n')


print('------EXEMPLO DE SLICE------')
print('Temos uma lista com 4 pessoas: João, Maria, José e Ana')
pessoas = ['João', 'Maria', 'José', 'Ana']
print(pessoas[1:3]) 
print(pessoas[0:1])
print(len(pessoas))
