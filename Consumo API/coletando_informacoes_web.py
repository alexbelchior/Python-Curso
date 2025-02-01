import requests
from bs4 import BeautifulSoup

# URL da página que desejamos capturar as informações
url = 'https://ge.globo.com'

# Faz a requisição para a página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemplo 1: Capturando o título da página
    title = soup.title.string if soup.title else 'Sem título'
    print("Título da página:", title)
    
    # Exemplo 2: Capturando todos os links (tags <a>)
    links = soup.find_all('a')
    print("\nLista de links encontrados:")
    for link in links:
        href = link.get('href')
        # Verifica se o link possui o atributo href
        if href:
            print(href)
else:
    print("Falha ao acessar a página. Código de status:", response.status_code)
