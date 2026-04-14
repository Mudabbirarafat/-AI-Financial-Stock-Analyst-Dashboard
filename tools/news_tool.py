import requests


def get_financial_news(company: str) -> str:
    """Fetch latest financial news"""

    url = f"https://newsapi.org/v2/everything?q={company}&pageSize=3&apiKey=demo"

    try:

        response = requests.get(url)

        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            return "No news found"

        titles = [a["title"] for a in articles]

        return "\n".join(titles)

    except Exception as e:

        return str(e)