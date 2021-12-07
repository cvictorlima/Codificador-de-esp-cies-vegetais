from bs4 import BeautifulSoup
import csv
import requests

url = 'http://www.arvoresbrasil.com.br/?pg=lista_especies&botao_pesquisa=1'

source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

soup = BeautifulSoup(source, 'lxml')

font = soup.find('font')
#print(font.prettify)

def cod(x):
    y = x.split()[0][:3].upper() + x.split()[1][:2].upper()
    return y

table = list()

rows = font.find_all('tr', class_='list')

for row in rows:
    items = row.find_all('td')
    item = [item.text.strip() for item in items]
    a, b, c, *_ = item
    d = cod(c)
    table.append([a, b, c, d])
    with open('especies.csv', 'a') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(['número', 'nome_popular', 'nome_cientifico', 'código'])

        for especie in table:
            csv_writer.writerow(especie)
print (table)