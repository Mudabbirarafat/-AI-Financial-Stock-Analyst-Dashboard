import requests

def load_sec_document(company_cik):

    url = f"https://data.sec.gov/submissions/CIK{company_cik}.json"

    headers = {
        "User-Agent": "financial-ai"
    }

    try:
        response = requests.get(url, headers=headers)

        data = response.json()

        filings = data.get("filings", {}).get("recent", {})

        text = str(filings)

        return text

    except Exception as e:

        return f"Error loading SEC document: {e}"