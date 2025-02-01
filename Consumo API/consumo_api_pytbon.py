import requests

# URL da API para buscar um post específico
url = "https://jsonplaceholder.typicode.com/posts/1"

# Fazendo a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Converte a resposta para o formato JSON
    dados = response.json()
    print("Dados recebidos:")
    print(dados)
    id_post = dados.get('id')
    title = dados.get('title')
    descricao = dados.get('body')
    print(f'Id: {id_post}')
    print(f'Título: {title}')
    print(f'Descrição: {descricao}')
else:
    print("Erro na requisição. Código de status:", response.status_code)