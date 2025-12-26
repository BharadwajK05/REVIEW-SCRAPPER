from datetime import datetime

def parse_date(date_str):
    """
    Convert date string to datetime object
    """
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d")
    except:
        return None


def is_date_in_range(review_date, start_date, end_date):
    """
    Check if review date is within range
    """
    return start_date <= review_date <= end_date


def clean_text(text):
    """
    Clean unwanted spaces and newlines
    """
    if text:
        return " ".join(text.split())
    return ""