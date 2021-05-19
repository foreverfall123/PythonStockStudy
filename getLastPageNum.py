from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, 'lxml')
pgrr = html.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]
print(last_page)
