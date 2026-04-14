from crewai import Agent
from utils.llm_setup import get_llm


def create_analyst_agent():

    return Agent(
        role="AI Investment Advisor",
        goal="Provide investment insights from the gathered stock data",
        backstory="Wall Street financial strategist",

        llm=get_llm(),

        allow_delegation=False,
        max_iter=1,
        verbose=True
    )