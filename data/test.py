import requests
import time
import json
from bs4 import BeautifulSoup


data_items = []

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_detail = soup.find_all("div",class_ = "job-description__item")
    i = 0
    for item in job_detail:
        print('item'+ str(i))
        content_text = item.get_text(strip=True)
        print(content_text)
        i+=1
    
    item = {
        "description": job_detail[0].get_text(strip=True),
        "requirement": job_detail[1].get_text(strip=True),
        "privilege":job_detail[2].get_text(strip=True),
        "place": job_detail[3].get_text(strip=True),
        "recruitment":job_detail[4].get_text(strip=True),
    }
    data_items.append(item)

    

def read_strings_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return None


def crawl_list():
    url_list = read_strings_from_json("./data2.json")
    for url in url_list:
        time.sleep(3)
        get_data(url)


if __name__ == "__main__":
    crawl_list()
    with open("final_data.json", "w", encoding='utf-8') as file:
        json.dump(data_items, file, indent=4, ensure_ascii=False)