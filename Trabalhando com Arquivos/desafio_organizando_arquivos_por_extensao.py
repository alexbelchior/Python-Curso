#Organizar os arquivos por formato
from pathlib import Path
import shutil
import datetime

pasta_atual = Path(__file__).parent
pasta_a_organizar = pasta_atual / 'Arquivos Desafio'
pasta_organizada = pasta_atual / 'Organizada'
pasta_backup = pasta_atual / 'Backup'

if pasta_organizada.exists():
    shutil.rmtree(pasta_organizada)

pasta_organizada.mkdir()

if not pasta_backup.exists():
    pasta_backup.mkdir()

for arquivo in pasta_a_organizar.glob('**/*'):
    if arquivo.is_file():
        pasta_organizada_com_extensao = pasta_organizada / arquivo.suffix.replace('.','')
        if not pasta_organizada_com_extensao.exists():
            pasta_organizada_com_extensao.mkdir()
        shutil.copy(arquivo, pasta_organizada_com_extensao)

nome_backup = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(pasta_backup / nome_backup, 'zip', pasta_organizada)