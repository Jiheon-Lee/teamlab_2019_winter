2주차 Crawling with Python
=========================

목표 : 크롤링과 관련된 개념을 이해하고 프로젝트에 필요한 데이터 수집 위한 크롤링 코드 작성 후 데이터를 수집해보고 csv 파일로 저장하기 (데이터는 .gitignore를 활용해보자) 2020.01.09 ~ 2020.01.15

Courses
-------

### Crawling with Python
- [파이썬입문과 크롤링기초 부트캠프](https://www.inflearn.com/course/Python-crawling-basic), 인프런, 2019
- [업무 자동화를 위한 파이썬 pyautogui, beautifulsoup 크롤링 기초](https://www.inflearn.com/course/%EC%97%85%EB%AC%B4%EC%9E%90%EB%8F%99%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-pyautogui-%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B8%B0%EC%B4%88#), 인프런, 2019
- [현존 최강 크롤링 기술: Scrapy와 Selenium 정복](https://www.inflearn.com/course/Crawling-Scrapy-Selenium#), 인프런, 2019

## 멜론(Melon) 실시간 인기차트 TOP 100
- **Crawling with python Code**<br>

```python
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
```

- **Melon DataFrame**<br><br>
![Melon_DataFrame](https://user-images.githubusercontent.com/48443734/72450063-08ac8900-37fd-11ea-9c48-a3ce058ac533.PNG)

- **Melon CSV**<br><br>
![Melon CSV](https://user-images.githubusercontent.com/48443734/72450244-5a551380-37fd-11ea-990e-8f24cb088bf7.PNG)

## 네이버(Naver) 연극 월/일/주간/주말 별 연극
- **Crawling with python Code**<br>

```python
from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
import pandas as pd

user_input = quote_plus(input('''-월--일, -월, 이번주, 이번주말 중 선택하여 입력해주세요.
                                 (-은 숫자 입력, 이번년도만 가능) : '''))
url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query={user_input}%20%EC%97%B0%EA%B7%B9%20%EA%B3%B5%EC%97%B0'
chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정
driver = webdriver.Chrome(chromedriver, options=options)

driver.get(url)

try:    # 정상 처리
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'list_title'))
    )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
    theater_list = []
    pageNum = int(driver.find_element_by_class_name('_totalCount').text)

    for i in range(1, pageNum):
        theater_data = driver.find_elements_by_class_name('list_title')

        for k in theater_data:
            theater_list.append(k.text.split('\n'))

        driver.find_element_by_xpath("//a[@class='btn_page_next _btnNext on']").click()
        time.sleep(2)

    driver.quit()

except TimeoutException:    # 예외 처리
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()

theater_df = pd.DataFrame(theater_list,
                          columns=['연극명', '기간', '장소'])
theater_df.index = theater_df.index + 1    # 인덱스 초기값 1로 변경
theater_df.to_csv('theater_df.csv', mode='w', encoding='utf-8-sig',
                  header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
```

- **Theater DataFrame**<br><br>
![Theater DataFrame](https://user-images.githubusercontent.com/48443734/72451373-2975de00-37ff-11ea-9170-905ee73c14e7.PNG)

- **Theater CSV**<br><br>
![Theater CSV](https://user-images.githubusercontent.com/48443734/72451415-3e527180-37ff-11ea-9644-279c078a515a.PNG)
