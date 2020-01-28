from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

theater_df = pd.read_csv('theater_df.csv')
search_word = theater_df['연극명'].values.tolist()

chromedriver = '/home/leejiheon/workspace/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EA%B7%B9%EC%A0%81%EC%9D%B8%ED%95%98%EB%A3%BB%EB%B0%A4')

detail_list = []
for i in search_word:
    search_input = driver.find_element_by_xpath('//*[@id="nx_query"]')
    search_input.clear()
    search_input.send_keys(i)
    search_click = driver.find_element_by_xpath('//*[@id="nx_search_form"]/fieldset/button')
    search_click.send_keys(Keys.RETURN)
    elem = driver.find_element_by_class_name('item_list')
    info = elem.text
    info_list = info.strip().split('\n')
    age = info_list[2]
    time = info_list[4]
    discription = info_list[-1]
    detail_list.append([i, age, time, discription])

driver.quit()

detail_df = pd.DataFrame(detail_list,
                         columns=['연극명', '관람등급', '공연시간', '내용'])
detail_df.to_csv('detail_df.csv', mode='w', encoding='utf-8-sig', header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
