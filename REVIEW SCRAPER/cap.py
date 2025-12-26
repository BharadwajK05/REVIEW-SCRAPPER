import requests
from bs4 import BeautifulSoup
from utils import parse_date, is_date_in_range, clean_text
import time

def scrape_capterra(company, start_date, end_date):
    reviews = []
    page = 1

    while True:
        url = f"https://www.capterra.com/p/{company.lower().replace(' ', '-')}/reviews/?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        review_blocks = soup.find_all("div", class_="review")

        if not review_blocks:
            break

        for block in review_blocks:
            try:
                title = clean_text(block.find("h3").text)
                review_text = clean_text(block.find("p").text)
                date_text = block.find("time").text.strip()
                review_date = parse_date(date_text)

                if not review_date:
                    continue

                if not is_date_in_range(review_date, start_date, end_date):
                    continue

                reviews.append({
                    "title": title,
                    "review": review_text,
                    "date": date_text,
                    "rating": "N/A",
                    "reviewer": "Anonymous"
                })
            except:
                continue

        page += 1
        time.sleep(1)

    return reviews