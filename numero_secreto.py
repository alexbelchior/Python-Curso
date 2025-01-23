numero_secreto = 19
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input('Digite um número: '))
        if chute < numero_secreto:
            print('O número secreto é maior')
        elif chute > numero_secreto:
            print('O número secreto é menor')
        else:
            print('Você acertou!')
            descobriu = True

