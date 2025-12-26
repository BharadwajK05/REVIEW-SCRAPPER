                                                          Product Review Scraper
                                                  ---------------------------------------

--> Overview

This project is a Python script that scrapes product reviews for a given company from SaaS review platforms such as G2 and Capterra within a specified date range.  
A third review source (Trustpilot) is also integrated as a bonus feature.

------------------------------------------------------------------------------------------------------------------------------------------

--> Features

Scrapes reviews from G2, Capterra, and Trustpilot
Accepts company name, start date, end date, and source as inputs
Filters reviews based on the given date range
Handles pagination
Outputs review data in JSON format

------------------------------------------------------------------------------------------------------------------------------------------

--> Project Structure

scraper.py – Main script
g2.py – G2 review scraper
cap.py – Capterra review scraper
thirdsource.py – Trustpilot scraper (bonus)
utils.py – Helper functions
output/reviews.json – Output file

------------------------------------------------------------------------------------------------------------------------------------------

## Requirements
Python 3.8+  
Required libraries:
pip install requests beautifulsoup4

------------------------------------------------------------------------------------------------------------------------------------------

## How to Run (Command Prompt)

1. Open Command Prompt
2. Navigate to the project folder:
   cd <project_folder_path>

3. Run the script:
   python scraper.py --company "<company_name>" --start_date YYYY-MM-DD --end_date YYYY-MM-DD --source <source>

### Example:
python scraper.py --company Notion --start_date 2023-01-01 --end_date 2023-12-31 --source g2

------------------------------------------------------------------------------------------------------------------------------------------

## Output
The script generates a JSON file at: output/reviews.json

------------------------------------------------------------------------------------------------------------------------------------------

## Bonus

A third SaaS review source (Trustpilot) has been integrated with the same input and output structure as G2 and Capterra, fulfilling the bonus requirement mentioned in the assignment.
------------------------------------------------------------------------------------------------------------------------------------------
