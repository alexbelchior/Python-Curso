import requests
from bs4 import BeautifulSoup

url = "https://www.dotabuff.com/heroes?show=heroes&view=winning"
headers = {"User-Agent": "Mozilla/5.0 ..."}  # Use um User-Agent válido

response = requests.get(url, headers=headers)
herois = []
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    rows = soup.select("tr.tw-border-b")  # seleciona todas as linhas desejadas
    for row in rows[:20]:  # itera apenas sobre os primeiros 20 elementos
        # Extrair o nome do herói (supondo que esteja dentro de uma <div> com a classe "tw-flex tw-flex-col tw-gap-0")
        name_div = row.select_one("td .tw-flex.tw-flex-col.tw-gap-0 div")
        hero_name = name_div.get_text(strip=True) if name_div else "Nome não encontrado"
        
        # Extrair o win rate do herói (supondo que esteja no <span> dentro de uma <div> com as classes específicas)
        win_rate_span = row.select_one("td:nth-of-type(2) div.tw-flex.tw-w-full.tw-flex-col.tw-items-start.tw-gap-1 span")
        win_rate = win_rate_span.get_text(strip=True) if win_rate_span else "Win rate não encontrado"
        tupla_heroi = (hero_name, win_rate)
        herois.append(tupla_heroi)
        print(f"Herói: {hero_name} - Win Rate: {win_rate}")
else:
    print("Erro ao acessar a página.")


print(herois)