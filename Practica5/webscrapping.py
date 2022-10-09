import requests
from bs4 import BeautifulSoup
pag = requests.get('http://scp-es.com/serie-scp-es')
soup = BeautifulSoup(pag.text, 'html.parser')
ubidedata = soup.find('div', class_="content-panel standalone series")
ListaDeScp = ubidedata.find_all('strong')
print('Lista de Scp´s')
for scp in ListaDeScp:
    print(scp.text)
