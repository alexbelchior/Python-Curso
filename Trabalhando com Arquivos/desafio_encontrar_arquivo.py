# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário

from pathlib import Path

def encontraArquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo: #caso queira pesquisar inclusive passando a extensão poderia utiliza arquivo.name
                print(arquivo)

print(Path.cwd())
encontraArquivo(Path.cwd(), 'arquivo')
