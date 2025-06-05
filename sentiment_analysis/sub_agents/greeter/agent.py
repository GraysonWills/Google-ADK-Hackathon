from google.adk.agents import Agent

from sentiment_analysis.sub_agents.greeter.prompt import TEST_AGENT_PROMPT

from sentiment_analysis.tools.load import memorize

greeter_agent = Agent(
    model="gemini-2.0-flash",
    name="greeter_agent",
    description="a sentiment analysis agent that greets the user",
    instruction=TEST_AGENT_PROMPT,
    tools=[memorize]
)