from pathlib import Path
import os

# Listando arquivos de uma pasta
print('Listando todos os arquivos do diretório home do usuário')
caminho = os.listdir(Path.home())
print(caminho)
print('---------------------------------')
print('')
print('Retornando todos os arquivos do diretório atual do usuário com o caminho absoluto')
caminho = list(Path.cwd().glob('*'))
print(caminho)
print('---------------------------------')
print('')

# Listando arquivos da pasta atual e de todas outras pastas a partir do diretório atual
print('Listando arquivos da pasta atual e das subpastas')
caminho = list(Path.cwd().glob('**/*'))
print(caminho)
print('---------------------------------')
print('')

# Listando arquivos com uma extensão específica
caminho = list(Path.cwd().glob('*.py'))
print(caminho)
print('---------------------------------')
print('')

# Validando um caminho
print('Validando um caminho')
caminho = Path.home() / 'nao_existe'
caminho_existe = caminho.exists
if caminho_existe == True:
    print('Diretório existe')
else:
    print('Diretório não existe')

print('---------------------------------')
print('')

# Verificando se é arquivo ou pasta
arquivo = Path(__file__)
verifica_arquivo = arquivo.is_file()

if verifica_arquivo == True:
    print(f'{arquivo} é um arquivo')

pasta = Path(__file__).parent
verifica_pasta = pasta.is_dir()

if verifica_pasta == True:
    print(f'{pasta} é uma pasta')

