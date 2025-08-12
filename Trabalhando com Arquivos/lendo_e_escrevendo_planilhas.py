from pathlib import Path
import pandas as pd

#Lendo tabelas com dataframe
pasta_atual = Path(__file__).parent
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')
print(tabela_clientes.head(10)) # Exibe as primeiras 10 linhas da tabela

#Lendo uma aba específica do arquivo excel
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SP')
print(tabela_clientes.head(10))

#Modificando header para não exibir a primeira linha
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', header=1)
print(tabela_clientes.head(10))

#Adicionando coluna de index
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', index_col=0)
print(tabela_clientes.head(10))

#Lendo colunas específicas do arquivo excel
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', usecols="A:B")
print(tabela_clientes.head(10))

#Lendo colunas específicas do arquivo excel [2]
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', usecols=['Nome', 'Email'])
print(tabela_clientes.head(10))

#Representando valores decimais
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', usecols=['Nome', 'Receita'], decimal='.') # informa que o separador decimal é o ponto
print(tabela_clientes.head(10))

#tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ', usecols=['Nome', 'Receita'], thousands='.')

#Escrevendo na planilha
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ')
tabela_clientes.to_excel(pasta_atual / 'clientes_atualizado.xlsx', index=False)

=======
#Escrevendo diversas abas
with pd.ExcelWriter(pasta_atual / 'clientes_atualizado.xlsx') as writer:
    tabela_clientes_SP = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SP')
    tabela_clientes_RJ = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RJ')
    tabela_clientes_SP.to_excel(writer, sheet_name='SP', index=False)
    tabela_clientes_RJ.to_excel(writer, sheet_name='RJ', index=False)
>>>>>>> 11813b41f9b0cac22fcfb2898f08039f019590e5
