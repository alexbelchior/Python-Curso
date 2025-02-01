from pathlib import Path
import os
import random
import string

# Define a pasta onde os arquivos serão criados
pasta_atual = Path(__file__).parent
caminho_pasta = pasta_atual / 'Arquivos Desafio'
quantidade = 10

def gerar_arquivos(extensao, quantidade, pasta):
    """ Gera arquivos com nomes aleatórios dentro de uma pasta específica. """
    
    pasta.mkdir(parents=True, exist_ok=True)  # Cria a pasta caso não exista

    for _ in range(quantidade):
        nome_arquivo = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + f'.{extensao}'
        caminho_arquivo = pasta / nome_arquivo  # Define o caminho do arquivo

        try:
            with caminho_arquivo.open('w', encoding='utf-8') as file:
                file.write('Arquivo gerado automaticamente\n')
            
            print(f'Arquivo {nome_arquivo} criado no diretório: {pasta}')
        
        except PermissionError:
            print(f"Permissão negada ao criar o arquivo: {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao criar o arquivo {caminho_arquivo}: {e}")

# Chamando a função
gerar_arquivos('pdf', quantidade, caminho_pasta)
