import streamlit as st
import yfinance as yf

from crew.crew_setup import run_analysis
from ml.stock_predictor import predict_stock_price
from tools.news_tool import get_financial_news

st.set_page_config(
    page_title="AI Financial Stock Analyst",
    layout="wide"
)

st.title("📊 AI Financial Stock Analyst Dashboard")

stock = st.text_input("Enter Stock Symbol (Example: TSLA, AAPL, NVDA)")

if st.button("Analyze"):

    if stock:

        # -------- Download stock data --------
        data = yf.download(stock, period="6mo")

        # Convert to float to avoid formatting errors
        latest_price = float(data["Close"].iloc[-1])
        previous_price = float(data["Close"].iloc[-2])
        change = latest_price - previous_price

        # ML prediction
        prediction = predict_stock_price(stock)

        # -------- Metrics Section --------
        col1, col2, col3 = st.columns(3)

        col1.metric(
            label="Current Price",
            value=f"${latest_price:.2f}",
            delta=f"{change:.2f}"
        )

        col2.metric(
            label="ML Predicted Price",
            value=f"${prediction:.2f}"
        )

        col3.metric(
            label="Model Confidence",
            value="Medium"
        )

        st.divider()

        # -------- Charts Section --------
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.subheader("📈 Stock Price (6 Months)")
            st.line_chart(data["Close"])

        with col_chart2:
            st.subheader("📊 Trading Volume")
            st.bar_chart(data["Volume"])

        st.divider()

        # -------- News Section --------
        st.subheader("📰 Latest Financial News")

        news = get_financial_news(stock)

        for article in news.split("\n"):
            st.write("•", article)

        st.divider()

        # -------- AI Analysis Section --------
        st.subheader("🤖 AI Investment Analysis")

        with st.spinner("AI analyzing market data..."):
            analysis = run_analysis(stock)

        st.success("Analysis Complete")

        st.write(analysis)