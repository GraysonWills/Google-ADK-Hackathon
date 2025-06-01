from google.adk.agents import Agent
from sentiment_analysis.tools.load import _load_precreated_itinerary
from sentiment_analysis.prompt import ROOT_AGENT_PROMPT

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=ROOT_AGENT_PROMPT,
    before_agent_callback=_load_precreated_itinerary,
)
