# Importando as bibliotecas necessárias para requisições HTTP, parsing HTML e manipulação de dados.
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definindo a palavra-chave que será usada na busca.
keyword = "Notebook"

# Montando a URL de busca com a palavra-chave.
url = f"https://lista.mercadolivre.com.br/{keyword}"

# Fazendo a requisição HTTP para obter o conteúdo da página.
response = requests.get(url)

# Verificando se a resposta foi bem-sucedida (status code 200).
if response.status_code == 200:
    # Interpretando o conteúdo HTML da resposta usando o BeautifulSoup.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscando todos os itens de produto na página (cada produto é um <li> com a classe especificada).
    items = soup.find_all("li", class_="ui-search-layout__item")
    
    # Criando uma lista vazia para armazenar os dados extraídos.
    data = []
    
    # Iterando sobre cada item encontrado.
    for item in items:
        # Definindo as tags que contêm as informações desejadas: título, link, preço e marca.
        title_tag = item.find("a", class_="poly-component__title")
        link_tag = item.find("a", class_="poly-component__title")
        price_tag = item.find("span", class_="andes-money-amount__fraction")
        brand_tag = item.find("span", class_="poly-component__brand")

        # Extraindo e limpando os textos das tags, ou definindo como "N/A" se não forem encontradas.
        title = title_tag.text.strip() if title_tag else "N/A"
        link = link_tag['href'] if link_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"
        brand = brand_tag.text.strip() if brand_tag else "N/A"
        
        # Adicionando o dicionário com as informações extraídas à lista de dados.
        data.append({"Title": title, "Brand": brand, "Price": price, "Link": link})
        
    # Exibindo os dados extraídos em formato de tabela usando o pandas DataFrame.
    print(pd.DataFrame(data))
    df_ml = pd.DataFrame(data)
else:
    # Se a resposta não foi bem-sucedida, imprimir mensagem de erro.
    print("Erro")

df_ml.to_csv("../data/notebooks_ml_scraping.csv", sep=";", index=False, encoding="utf-8")

