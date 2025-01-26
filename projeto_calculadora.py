import os

continuar = True

while continuar:
    print('Escolha a operação que deseja realizar:')
    print('+ - Soma')
    print('- - Subtração')
    print('* - Multiplicação')
    print('/ - Divisão')
    print('^ - Exponenciação')
    print('---------------------------------')

    operacao = input('Digite a operação desejada: ')

    def soma(x, y):
        return x + y

    def subtracao(x, y):
        return x - y

    def multiplicacao(x, y):
        return x * y

    def divisao(x, y):
        return x / y

    def exponenciacao(x, y):
        return x ** y
    
    def continuar():
        resposta = input('Deseja continuar? (s/n) ')
        if resposta == 'n':
            os.system('cls') # Limpa a tela no Windows
            return False
        elif resposta == 's':
            os.system('cls') # Limpa a tela no Windows
            return True
        else:
            print('Resposta inválida!')
            continuar()

    if operacao == '+':
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        print(f'O resultado da soma é: {soma(x, y)}')
        continuar()
    elif operacao == '-':
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        print(f'O resultado da subtração é: {subtracao(x, y)}')
        continuar()
    elif operacao == '*':
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        print(f'O resultado da multiplicação é: {multiplicacao(x, y)}')
        continuar()
    elif operacao == '/':
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        if y == 0:
            print('Não é possível dividir por zero!')
            continuar()
        else:    
            print(f'O resultado da divisão é: {divisao(x, y)}')
            continuar()
    elif operacao == '^':
        x = float(input('Digite a base: '))
        y = float(input('Digite o expoente: '))
        print(f'O resultado da exponenciação é: {exponenciacao(x, y)}')
        continuar()
    else:
        print('Operação inválida!')