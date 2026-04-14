from crewai import Agent
from tools.stock_tool import get_stock_price
from utils.llm_setup import get_llm


def create_market_agent():

    return Agent(
        role="Market Data Analyst",
        goal="Fetch the latest stock price using the stock tool",
        backstory="Expert financial market analyst",

        tools=[get_stock_price],

        llm=get_llm(),

        allow_delegation=False,
        max_iter=1,
        verbose=True
    )