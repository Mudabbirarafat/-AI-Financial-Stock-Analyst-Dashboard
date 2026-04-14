import requests


def get_sec_filings(company: str) -> str:
    """Fetch SEC filing data"""

    url = f"https://data.sec.gov/submissions/CIK{company}.json"

    headers = {
        "User-Agent": "financial-ai"
    }

    try:

        response = requests.get(url, headers=headers)

        data = response.json()

        return str(data.get("filings", {}).get("recent", {}))

    except Exception as e:

        return str(e)