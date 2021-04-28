import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nba.com/news'

headers = {
'Host': 'www.nba.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'
}
response = requests.get(url, headers=headers)

html = response.content.decode('utf-8')

soup = BeautifulSoup(html, 'lxml').find('div', class_='flex flex-col lg:mr-3 lg:w-3/4').find_all('li')

a = []
b = []
c = []

for ul in soup:
    try :
        title = ul.find('h2', class_='t1 group-hover:underline').text
        jianjie = ul.find('p', class_='t6 pt-2').text
        shijian = ul.find('span', class_='t9 text-asphalt').text
        print(title)
        print(jianjie)
        print(shijian)
        a.append(title)
        b.append(jianjie)
        c.append(shijian)
    except:
        pass


df=pd.DataFrame({'title':a,'Introduction ':b,'time':c})
print(df)


