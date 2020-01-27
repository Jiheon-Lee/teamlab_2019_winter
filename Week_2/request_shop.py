from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import pandas as pd

user_input = quote_plus(input('최저가 연극 관람 티켓을 찾을 검색어를 입력해주세요 : '))
url = f'https://search.shopping.naver.com/search/all.nhn?query={user_input}&cat_id=&frm=NVSHATC'
chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get(url)

try:    # 정상 처리
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_itemSection'))
    )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
    shop_list = []
    elem = driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li[1]/div[2]/div/a')
    purchase_name = elem.text
    purchase_link = elem.get_attribute('href')
    elem = driver.find_element_by_css_selector('#_search_list > div.search_list.basis > ul > li:nth-child(1) > div.info > span.price > em > span.num._price_reload')
    purchase_price = elem.text
    shop_list.append([purchase_name, purchase_price, purchase_link])

except TimeoutException:    # 예외 처리
    print('해당 페이지에 최저가 연극 관람 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()

shop_df = pd.DataFrame(shop_list,
                       columns=['Title', 'Price', 'link'])
shop_df.to_csv('req_shop_df.csv', mode='a', encoding='utf-8-sig',
               header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
