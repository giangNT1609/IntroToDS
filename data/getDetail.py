import requests
import time
import json
from bs4 import BeautifulSoup


data_items = []

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_detail = soup.find_all("div",class_ = "job-description__item")
    item = {
        "description": job_detail[0].find("div", class_="job-description__item--content").get_text(strip=True) if len(job_detail) > 0 else '',
        "requirement": job_detail[1].find("div", class_="job-description__item--content").get_text(strip=True) if len(job_detail) > 0 else '',
        "privilege":job_detail[2].find("div", class_="job-description__item--content").get_text(strip=True) if len(job_detail) > 0 else '',
        "place": job_detail[3].find("div", class_="job-description__item--content").get_text(strip=True) if len(job_detail) > 0 else '',
        "recruitment":job_detail[4].find("div", class_="job-description__item--content").get_text(strip=True) if len(job_detail) > 0 else '',
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
    url_list = read_strings_from_json("./data.json")
    for url in url_list:
        get_data(url)
        time.sleep(3)


if __name__ == "__main__":
    crawl_list()
    with open("final_data.json", "w", encoding='utf-8') as file:
        json.dump(data_items, file, indent=4, ensure_ascii=False)