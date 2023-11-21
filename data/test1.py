import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Set up Selenium options and the Chrome driver
options = Options()
driver = webdriver.Chrome(options=options)

# Make a GET request to the web page
url = 'https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?sort=up_top'
driver.get(url)

pageNumberMax = 10

items = []

i = 1
while i <= pageNumberMax:
    # Scroll to the bottom of the page to load more job items
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the elements to be loaded
    wait = WebDriverWait(driver, 10)
    try:
        elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-list-search-result')))
        time.sleep(random.nextInt(2000))
    except:
        print("No job items found on page", i)
        break

    # Print the extracted data
    for element in elements:
        link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        items.append(link)
        print(link)

    # Go to the next page
    i += 1
    driver.get(url + "&page=" + str(i))

# Save the data to a JSON file
with open("data1.json", "w", encoding='utf-8') as file:
    json.dump(items, file, indent=4, ensure_ascii=False)

# Close the browser
driver.quit()
