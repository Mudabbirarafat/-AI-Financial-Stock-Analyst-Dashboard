from crewai import Agent
from tools.sec_tool import get_sec_filings
from utils.llm_setup import get_llm


def create_sec_agent():

    return Agent(
        role="SEC Filing Analyst",
        goal="Analyze SEC filings using the SEC tool",
        backstory="Expert in financial compliance reports",

        tools=[get_sec_filings],

        llm=get_llm(),

        allow_delegation=False,
        max_iter=1,
        verbose=True
    )