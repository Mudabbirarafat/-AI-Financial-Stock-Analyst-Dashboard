# Financial AI Analyst

AI-powered Streamlit dashboard for quick stock analysis.  
It combines market data, a simple ML forecast, latest news headlines, SEC filing snippets, and an LLM-generated investment summary.

## Features

- Live stock data (6-month trend + latest price) via `yfinance`
- Basic next-step price prediction using `LinearRegression`
- Recent financial headlines from NewsAPI
- SEC filing data lookup from SEC submissions API
- AI-generated analysis using Groq (`llama-3.1-8b-instant`)
- Interactive Streamlit UI with charts and metrics

## Tech Stack

- Python
- Streamlit
- yfinance
- scikit-learn
- requests
- langchain-groq

## Project Structure

`app.py` - Main Streamlit app  
`crew/crew_setup.py` - Orchestrates data collection and final analysis prompt  
`utils/llm_setup.py` - LLM wrapper (`llm.call(prompt)` interface)  
`ml/stock_predictor.py` - Linear regression price prediction  
`tools/stock_tool.py` - Latest stock price helper  
`tools/news_tool.py` - Financial news helper  
`tools/sec_tool.py` - SEC filings helper

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd financial-ai-analyst
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## How It Works

1. User enters a stock ticker (e.g., `AAPL`, `TSLA`, `NVDA`).
2. App downloads recent market data.
3. ML module predicts a near-term price.
4. News + SEC helper tools fetch external context.
5. Combined context is sent to the LLM for a short investment analysis.
6. Dashboard displays metrics, charts, headlines, and AI output.

## Notes

- Current news tool uses NewsAPI `demo` key in code. For reliable results, replace it with your own API key.
- Some files under `agents/` still import `crewai`; the main app flow currently works through `crew/crew_setup.py` and `utils/llm_setup.py`.

## Future Improvements

- Add robust error handling for invalid tickers / API failures
- Improve SEC lookup (CIK normalization and mapping)
- Add model confidence scoring from data, not static text
- Add test coverage for tools and analysis pipeline
