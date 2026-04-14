import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_stock_price(ticker):

    data = yf.download(ticker, period="6mo")

    data["Day"] = np.arange(len(data))

    X = data[["Day"]]
    y = data["Close"]

    model = LinearRegression()

    model.fit(X, y)

    next_day = np.array([[len(data) + 1]])

    prediction = model.predict(next_day)

    return float(prediction[0])