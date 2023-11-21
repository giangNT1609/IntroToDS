from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
import time
import random

# Set up Selenium options and the Chrome driver
options = Options()
driver = webdriver.Chrome(options=options)

# Make a GET request to the web page
url = 'https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?sort=up_top'
driver.get(url)

pageNumberMax = 2

items = []

i = 1
while i< pageNumberMax:
    y = 2300
    while y <= 6000:
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
    time.sleep(random.randint(2,5))
# Wait for the elements to be loaded
    wait = WebDriverWait(driver, 1000)
    elements = driver.find_elements(By.CLASS_NAME,'job-list-search-result')
# Print the extracted data

    for element in elements:
        avatar_div = element.find_element(By.CLASS_NAME,'avatar')
        link = avatar_div.find_element(By.TAG_NAME, 'a').get_attribute('href')
        items.append(link)

    driver.get(url+"&page="+str(i))
# increase page
    i+=1

    with open("data1.json", "w", encoding='utf-8') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)

#Close the browser
driver.quit()