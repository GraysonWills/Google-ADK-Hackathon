from google.adk.agents import Agent
from sentiment_analysis.sub_agents.scheduler.prompt import SCHEDULER_AGENT_PROMPT
from sentiment_analysis.tools.load import memorize


scheduler_agent = Agent(
    model="gemini-2.0-flash",
    name="scheduler_agent",
    instruction=SCHEDULER_AGENT_PROMPT,
    description="You are a scheduler agent. You are responsible for scheduling future interactions to assess the sentiment of a piece of content.",
    tools=[memorize]

)