from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

theater_df = pd.read_csv('theater_df.csv')

chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://shopping.naver.com')

search_word = theater_df['연극명'].values.tolist()

shop_list = []
for i in search_word:
    search_input = driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
    search_input.clear()
    search_input.send_keys(i)
    search_click = driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]')
    search_click.send_keys(Keys.RETURN)
    elem = driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li[1]/div[2]/div/a')
    purchase_name = elem.text
    purchase_link = elem.get_attribute('href')
    elem = driver.find_element_by_css_selector('#_search_list > div.search_list.basis > ul > li:nth-child(1) > div.info > span.price > em > span.num._price_reload')
    purchase_price = elem.text
    shop_list.append([purchase_name, purchase_price, purchase_link])
    time.sleep(2)

driver.quit()

shop_df = pd.DataFrame(shop_list,
                       columns=['Title', 'Price', 'link'])
shop_df.to_csv('shop_df.csv', mode='w', encoding='utf-8-sig',
               header=True, index=True)
