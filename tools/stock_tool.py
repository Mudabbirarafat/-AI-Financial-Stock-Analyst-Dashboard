import yfinance as yf


def get_stock_price(ticker: str) -> str:
    """Fetch latest stock price"""

    stock = yf.Ticker(ticker)

    hist = stock.history(period="1d")

    if hist.empty:
        return "Stock data not found"

    price = hist["Close"].iloc[-1]

    return f"Latest price of {ticker} is ${price}"