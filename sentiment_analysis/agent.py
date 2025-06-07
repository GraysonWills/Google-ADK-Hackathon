from google.adk.agents import Agent
from sentiment_analysis.tools.load import _load_precreated_itinerary
from sentiment_analysis.prompt import ROOT_AGENT_PROMPT
from sentiment_analysis.sub_agents.greeter.agent import greeter_agent
from sentiment_analysis.sub_agents.audio.agent import audio_pipeline_agent
from sentiment_analysis.sub_agents.video.agent import video_pipeline_agent

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=ROOT_AGENT_PROMPT,
    sub_agents=[greeter_agent, video_pipeline_agent],
    before_agent_callback=_load_precreated_itinerary,
)
