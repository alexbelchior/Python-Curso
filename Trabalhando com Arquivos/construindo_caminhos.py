from pathlib import Path

caminho = Path('Primeira_Pasta')

print(caminho)


# Retornando caminho do diretório de trabalho atual
print(Path.cwd())

# Verificar se o caminho é absoluto
print(Path.cwd().is_absolute())

# Retornando o caminho da Primeira_Pasta
print(Path('Primeira_Pasta'))
print(Path('Primeira_Pasta').is_absolute())

# Transformando o caminha da Primeira_Pasta em absoluto
print(Path.cwd() / 'Trabalhando com Arquivos' / 'Primeira_Pasta')

# Verificando se o caminho existe
print((Path.cwd() / 'Trabalhando com Arquivos' / 'Primeira_Pasta').exists())

# Garantindo que estamos retornando o caminho para a pasta do script
print('-----------------------------')
print('Retornando o caminho da pasta do script')
print(__file__)
print(Path(__file__)) # O Path() retorna o caminho com barra invertida ou não identificando o sistema operacional
print('-----------------------------')
# Retornando a pasta acima
print(Path(__file__).parent)
print(Path(__file__).parent / 'Primeira_Pasta')
print('-----------------------------')
# Para retornar a pasta raiz do sistema
print('Retornando a pasta raiz do sistema')
caminho = Path(__file__)
print(caminho.anchor)
print('-----------------------------')

# Pegar apenas o nome do arquivo com a extensão
print('Pegando o nome do arquivo com extensão')
print(caminho.name)
print('-----------------------------')

# Pegar apenas o nome do arquivo sem a extensão
print('Pegando o nome do arquivo sem a extensão')
print(caminho.stem)
print('-----------------------------')

# Pegar a extensão do arquivo
print('Pegando a extensão do arquivo')
print(caminho.suffix)
print('-----------------------------')

# Retornando várias pastas acima
print('Retornando várias pastas acima')
print(caminho.parents[1])
print('-----------------------------')