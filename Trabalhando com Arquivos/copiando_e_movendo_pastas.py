from pathlib import Path
import os
import shutil

# Criando pasta
pasta_atual = Path(__file__).parent
pasta_destino = pasta_atual / 'Outra Pasta'
pasta_destino.mkdir(exist_ok=True) # verifica se a pasta já existe e evita a criação e evita erro no console

# Criando pasta com outra pasta dentro
pasta_atual = Path(__file__).parent
pasta_destino = pasta_atual / 'Outra Pasta' / 'Outra Pasta 2'
pasta_destino.mkdir(parents=True) # garante que a pasta seja criada mesmo que a pasta pai não exista

# Copiando pastas
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'Primeira_Pasta', pasta_atual / 'Primeira_Pasta' / 'Segunda_Pasta')

# Deletando pastas vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'Outra Pasta'
pasta_remover.rmdir() # Esse método só remove pastas vazias

# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'Outra Pasta'
shutil.rmtree(pasta_remover)