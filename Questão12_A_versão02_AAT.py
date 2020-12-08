#12-A IMPRIMA O CONTEÚDO REFERENTE APENAS À TABELA APRESENTADA NA PÁGINA INDICADA.
import requests
from bs4 import BeautifulSoup
import pandas as pd
 
 
def data(x):
    data_lines = x.text.replace('\n','//')[2:-2].split('//')
    return data_lines

file = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
html = requests.get(file).text
soup = BeautifulSoup(html, "lxml")

title = []
lines = []

for table in soup.find_all('div', class_='tabela'):
    for title_line in table.find_all('div', class_='titulo'):
        title.append(data(title_line))
    
    for line in table.find_all('div', class_='linha'):
        lines.append(data(line))

df = pd.DataFrame(data=lines, columns=title)
print(df)
