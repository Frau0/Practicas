import requests
from bs4 import BeautifulSoup
pag = requests.get('http://scp-es.com/serie-scp-es')
soup = BeautifulSoup(pag.text, 'html.parser')
ubidedata = soup.find('div', class_="content-panel standalone series")
ListaDeScp = ubidedata.find_all('strong')
arc = open('Lista de scps.txt', 'w')
arc.write('Lista de Scp´s\n')
for scp in ListaDeScp:
    arc.write(scp.text +'\n')
arc.close()
