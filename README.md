# REVIEW-SCRAPPER

🎯 Product Review Scraper Platform
======================================

A Python-based application that allows users to scrape product reviews from popular SaaS platforms and generate structured JSON outputs based on a given company and date range.

---

📌 Features
-----------
- Scrape product reviews from **G2** and **Capterra**
- Bonus integration with **Trustpilot**
- Filter reviews using **start date and end date**
- Handle pagination to fetch multiple reviews
- Clean and structured **JSON output**
- Graceful error handling for blocked or missing data

---

🛠 Tech Stack
-------------
**Backend**
- Python 3
- Requests
- BeautifulSoup (bs4)

**Data Handling**
- JSON
- Datetime utilities

---

📂 Project Structure
-------------------
scraper.py 
g2.py 
cap.py 
thirdsource.py 
utils.py 
output/
└── reviews.json # Generated output file
README.md

---

▶️ How to Run
-------------
1. Open **Command Prompt**
2. Navigate to the project directory:
cd <project_folder_path>

markdown
Copy code

3. Run the script:
python scraper.py --company "<company_name>" --start_date YYYY-MM-DD --end_date YYYY-MM-DD --source <source>

shell
Copy code

### Example
python scraper.py --company Notion --start_date 2023-01-01 --end_date 2023-12-31 --source g2

---

📤 Output
---------
- Reviews are saved in:
output/reviews.json

- Each review includes:
  - Title
  - Review text
  - Date
  - Rating (if available)
  - Reviewer name

---

⭐ Bonus Implementation
----------------------
- Integrated **Trustpilot** as a third SaaS review source
- Provides fallback data when scraping is blocked

---
