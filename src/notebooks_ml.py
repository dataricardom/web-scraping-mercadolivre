import pandas as pd

df = pd.read_csv("../data/notebooks_ml_scraping.csv", sep=";", encoding="utf-8")

print(df.groupby(by=["Brand"], as_index=False)[["Price"]]
        .mean()
        .sort_values(by="Price",ascending=False))

#Obtendo qual a media maior valor em R$ de produtos agrupados por marca.

marcas_maior_valor_medio = (df.groupby(by=["Brand"], as_index=False)[["Price"]]
        .mean()
        .sort_values(by="Price",ascending=False))

#Salvando Resultando em um novo arquivo .csv

try:
    print("Iniciando salvamento de arquivo:\n")
    salvar = marcas_maior_valor_medio.to_csv("../data/maior_media_valor_produtos_marca.csv", sep=";")
    print("\nSalvo com sucesso!")

except:
    print("\nErro ao salvar arquivo.")