import streamlit as st
import yfinance as yf

from crew.crew_setup import run_analysis
from ml.stock_predictor import predict_stock_price
from tools.news_tool import get_financial_news


def dashboard():

    st.set_page_config(
        page_title="AI Financial Stock Analyst",
        page_icon="📊",
        layout="wide"
    )

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("📊 AI Financial Analyst")

    page = st.sidebar.radio(
        "Navigation",
        ["Stock Analysis", "Market Overview", "About"]
    )

    # ---------------- HERO ----------------
    st.markdown(
        """
        <h1 style='text-align:center;'>📊 AI Financial Stock Analyst</h1>
        <p style='text-align:center;font-size:18px;color:gray'>
        AI-powered stock analysis using market data, machine learning prediction, and financial news.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # ---------------- FEATURES ----------------
    col1, col2, col3 = st.columns(3)

    col1.info("📈 Real-time stock market data")
    col2.info("🔮 Machine learning price prediction")
    col3.info("🤖 AI investment insights")

    st.write("")
    st.write("")

    # ---------------- STOCK ANALYSIS PAGE ----------------
    if page == "Stock Analysis":

        stock = st.text_input(
            "Enter Stock Symbol",
            placeholder="Example: TSLA, AAPL, NVDA"
        )

        analyze = st.button("🚀 Analyze Stock")

        if analyze and stock:

            data = yf.download(stock, period="6mo")

            latest_price = float(data["Close"].iloc[-1])
            previous_price = float(data["Close"].iloc[-2])
            change = latest_price - previous_price

            prediction = predict_stock_price(stock)

            st.divider()

            # -------- METRICS --------
            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Current Price",
                f"${latest_price:.2f}",
                f"{change:.2f}"
            )

            col2.metric(
                "ML Predicted Price",
                f"${prediction:.2f}"
            )

            col3.metric(
                "Model Confidence",
                "Medium"
            )

            st.write("")

            # -------- CHARTS --------
            col_chart1, col_chart2 = st.columns(2)

            with col_chart1:
                st.subheader("📈 Stock Price (6 Months)")
                st.line_chart(data["Close"])

            with col_chart2:
                st.subheader("📊 Trading Volume")
                st.bar_chart(data["Volume"])

            st.write("")

            # -------- NEWS --------
            st.subheader("📰 Latest Financial News")

            news = get_financial_news.func(stock)

            for article in news.split("\n"):
                st.write("•", article)

            st.write("")

            # -------- AI ANALYSIS --------
            st.subheader("🤖 AI Investment Analysis")

            with st.spinner("AI analyzing market data..."):
                result = run_analysis(stock)

            st.success("Analysis Complete")

            st.write(result)

    # ---------------- MARKET PAGE ----------------
    elif page == "Market Overview":

        st.header("🌎 Market Overview")

        st.write(
            "This section can show overall market indices such as S&P 500, Nasdaq, and Dow Jones."
        )

        st.info("Feature coming soon: Global market dashboard")

    # ---------------- ABOUT PAGE ----------------
    elif page == "About":

        st.header("ℹ️ About This Project")

        st.write(
            """
            This AI Financial Stock Analyst uses multiple technologies:

            • Generative AI (Groq Llama models)  
            • Machine Learning for stock prediction  
            • Financial APIs for market data  
            • News analysis for market insights  
            • Streamlit dashboard for visualization  

            The goal is to help users analyze stocks using AI-driven insights.
            """
        )