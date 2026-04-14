from tools.stock_tool import get_stock_price
from tools.news_tool import get_financial_news
from tools.sec_tool import get_sec_filings
from utils.llm_setup import get_llm


def run_analysis(stock):

    llm = get_llm()

    price = get_stock_price(stock)
    news = get_financial_news(stock)
    sec_data = get_sec_filings(stock)

    prompt = f"""
You are a financial analyst.

Stock: {stock}

Stock Price:
{price}

News:
{news}

SEC Data:
{sec_data}

Provide a short investment analysis.
"""

    response = llm.call(prompt)

    return response