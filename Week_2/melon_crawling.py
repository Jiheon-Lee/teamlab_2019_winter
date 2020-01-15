import requests
from bs4 import BeautifulSoup
import pandas as pd
hdr = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'
req = requests.get(url, headers=hdr)
soup = BeautifulSoup(req.content, 'html.parser')
lst_data = soup.select('.lst50, .lst100')
melon_lst = []
for i in lst_data:
    temp = []
    temp.append(i.select_one('.rank').text)
    temp.append(i.select_one('.rank01').a.text)
    temp.append(i.select_one('.rank02').a.text)
    temp.append(i.select_one('.rank03').a.text)
    melon_lst.append(temp)
melon_df = pd.DataFrame(melon_lst,
                        columns=['순위', '노래명', '아티스트', '앨범명'])
melon_df.to_csv('melon_100.csv', mode='w', encoding='utf-8-sig',
                header=True, index=False)
