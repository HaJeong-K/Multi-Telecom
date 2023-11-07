import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

import pandas as pd
import time
import pandas as pd
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://help.kt.com/store/KtStoreSearch.do"
driver.get(url)
time.sleep(3)
place_types = []
place_names = []
addresses = []
phones = []

# 기본 설정
select_element = driver.find_element(By.XPATH, '//*[@id="cfmClContents"]/div[2]/div/div/div/ul/li[2]/a')
select_element.click()

search_input = driver.find_element(By.XPATH, '//*[@id="trigger1-2"]/div/div[1]/input')
search_input.send_keys('서울')
time.sleep(1)

search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div/ul/li[2]/div/div/button')
search_button.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500)")

for i in range(0, 10):

        place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
        place_types.append(place_element.text)

        title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
        place_names.append(title_button.text)

        address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
        addresses.append(address_element.text)

        phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
        phones.append(phone_element.text)

xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div/div/a[1]'
wait = WebDriverWait(driver, 2)
next_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
next_button.click()
time.sleep(2)

for i in range(0, 10):

        place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
        place_types.append(place_element.text)

        title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
        place_names.append(title_button.text)

        address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
        addresses.append(address_element.text)

        phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
        phones.append(phone_element.text)


for _ in range(15):
        xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div/div/a[4]'
        wait = WebDriverWait(driver, 2)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        next_button.click()
        time.sleep(2)

        for i in range(0, 10):

                place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
                place_types.append(place_element.text)

                title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
                place_names.append(title_button.text)

                address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
                addresses.append(address_element.text)

                phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
                phones.append(phone_element.text)
                
        xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div/div/a[5]'
        wait = WebDriverWait(driver, 2)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        next_button.click()
        time.sleep(2)

        for i in range(0, 10):

                place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
                place_types.append(place_element.text)

                title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
                place_names.append(title_button.text)

                address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
                addresses.append(address_element.text)

                phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
                phones.append(phone_element.text)

        xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div/div/a[3]'
        wait = WebDriverWait(driver, 2)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        next_button.click()
        time.sleep(2)

        for i in range(0, 10):

                place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
                place_types.append(place_element.text)

                title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
                place_names.append(title_button.text)

                address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
                addresses.append(address_element.text)

                phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
                phones.append(phone_element.text)

xpath = '/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div/div/a[4]'
wait = WebDriverWait(driver, 2)
next_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
next_button.click()
time.sleep(2)

for i in range(0, 5):

        place_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[2]')
        place_types.append(place_element.text)

        title_button = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[3]')
        place_names.append(title_button.text)

        address_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[4]')
        addresses.append(address_element.text)

        phone_element = driver.find_element(By.XPATH, f'//*[@id="cfmClContents"]/div[3]/div/div/div[1]/div[3]/div[1]/div[1]/div[{i+1}]/div[5]')
        phones.append(phone_element.text)

data = {'장소타입': place_types,'장소': place_names, '주소': addresses, '전화번호': phones}
df = pd.DataFrame(data)

df.to_excel('KT.xlsx', index=False)
print(df)