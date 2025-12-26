import requests
from bs4 import BeautifulSoup
from utils import parse_date, is_date_in_range, clean_text
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_g2(company, start_date, end_date):
    reviews = []
    page = 1

    while True:
        url = f"https://www.g2.com/products/{company.lower().replace(' ', '-')}/reviews?page={page}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        review_blocks = soup.select("div[data-testid='review']")

        if not review_blocks:
            break

        for block in review_blocks:
            try:
                title = clean_text(block.find("h3").text)

                review_text = clean_text(
                    block.select_one("div[itemprop='reviewBody']").text
                )

                date_text = block.find("time")["datetime"][:10]
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