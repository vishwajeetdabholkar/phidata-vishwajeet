from phi.agent import Agent, RunResponse  # noqa
from phi.model.google import GeminiOpenAIChat

agent = Agent(model=GeminiOpenAIChat(id="gemini-1.5-flash"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
