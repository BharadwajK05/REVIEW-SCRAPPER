import argparse
import json
from datetime import datetime
from g2 import scrape_g2
from cap import scrape_capterra
from thirdsource import scrape_trustpilot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--start_date", required=True)
    parser.add_argument("--end_date", required=True)
    parser.add_argument("--source", required=True)

    args = parser.parse_args()

    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d")

    source = args.source.lower()

    if source == "g2":
        reviews = scrape_g2(args.company, start_date, end_date)
    elif source == "capterra":
        reviews = scrape_capterra(args.company, start_date, end_date)
    elif source == "trustpilot":
        reviews = scrape_trustpilot(args.company, start_date, end_date)
    else:
        print("Invalid source")
        return

    with open("output/reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4)

    print(f"{len(reviews)} reviews saved successfully")

if __name__ == "__main__":
    main()