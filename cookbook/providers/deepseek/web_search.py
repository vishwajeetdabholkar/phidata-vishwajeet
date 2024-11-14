"""Run `pip install duckduckgo-search` to install dependencies."""

from phi.agent import Agent
from phi.model.deepseek import DeepSeekChat
from phi.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=DeepSeekChat(id="deepseek-chat"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
