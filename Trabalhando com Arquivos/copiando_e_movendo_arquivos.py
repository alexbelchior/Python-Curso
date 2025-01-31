from pathlib import Path
import shutil
import os

# Copiando arquivo com copyfile (Não leva as permissões do arquivo)
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto1.txt'
caminho_arquivo_destino = pasta_atual / 'Primeira_Pasta' / 'texto1_copia.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)

# Copiando arquivo com copy
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto1.txt'
caminho_arquivo_destino = pasta_atual / 'Primeira_Pasta'

shutil.copy(caminho_arquivo, caminho_arquivo_destino) # Os parâmetros são qual o arquivo e qual a pasta, diferente do copyfile

# Copiando arquivo com copy2
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto1.txt'
caminho_arquivo_destino = pasta_atual / 'Primeira_Pasta'

shutil.copy2(caminho_arquivo, caminho_arquivo_destino) # Copy2 leva informação dos metadados, usuário que criou, data de criação etc

# Movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto1.txt'
caminho_arquivo_destino = pasta_atual / 'Primeira_Pasta' / 'Segunda_Pasta'

shutil.move(caminho_arquivo, caminho_arquivo_destino)


# Deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto1.txt'
os.remove(caminho_arquivo)