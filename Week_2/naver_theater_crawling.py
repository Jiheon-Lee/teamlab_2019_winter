from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
import pandas as pd

input = input('''-월--일, -월, 이번주, 이번주말 중 선택하여 입력해주세요.
                                 (-은 숫자 입력, 이번년도만 가능) : ''')
user_input = quote_plus(input)

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
    count = 0

    for i in range(1, pageNum):
        theater_data = driver.find_elements_by_class_name('list_title')
        img_data = driver.find_elements_by_class_name('list_thumb')

        for k in theater_data:
            theater_list.append(k.text.split('\n'))
            
        for j in img_data:
            count += 1
            j.screenshot(f'img/{count}.png')

        driver.find_element_by_xpath("//a[@class='btn_page_next _btnNext on']").click()
        time.sleep(2)

except TimeoutException:    # 예외 처리
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()

theater_df = pd.DataFrame(theater_list,
                          columns=['연극명', '기간', '장소'])
theater_df.index = theater_df.index + 1    # 인덱스 초기값 1로 변경
theater_df.to_csv(f'theater_{input}_df.csv', mode='w', encoding='utf-8-sig',
                  header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
