from crewai import Agent
from tools.news_tool import get_financial_news
from utils.llm_setup import get_llm


def create_news_agent():

    return Agent(
        role="Financial News Analyst",
        goal="Find financial news using the provided news tool only",
        backstory="Expert in financial journalism",

        tools=[get_financial_news],

        llm=get_llm(),

        allow_delegation=False,
        max_iter=1,
        verbose=True
    )