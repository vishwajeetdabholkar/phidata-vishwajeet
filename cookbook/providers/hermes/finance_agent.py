"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.ollama import Hermes
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=Hermes(id="hermes3"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
)

# agent.print_response("Share the NVDA stock price and analyst recommendations", stream=True)
agent.print_response("Summarize fundamentals for TSLA", stream=True)
