from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from sentiment_analysis.tools.load import _load_precreated_itinerary
from sentiment_analysis.prompt import ROOT_AGENT_PROMPT, TOTAL_ANALYSIS_AGENT_PROMPT
from sentiment_analysis.sub_agents.greeter.agent import greeter_agent
from sentiment_analysis.sub_agents.audio.agent import (
  
    audio_pitch_agent,
    audio_speed_agent,
    audio_transcript_agent,
 
)
from sentiment_analysis.sub_agents.video.agent import (

    facial_analysis_agent,
    body_posture_agent,

)

parallel_analysis_agent = ParallelAgent(
    name="parallel_analysis_agent",
    sub_agents=[
        audio_pitch_agent,
        audio_speed_agent,
        audio_transcript_agent,
        facial_analysis_agent,
        body_posture_agent,
    ],
)

total_output_agent = Agent(
    model="gemini-2.0-flash",
    name="total_output_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=TOTAL_ANALYSIS_AGENT_PROMPT,
)

sequential_analysis_agent = SequentialAgent(
    name="sequential_analysis_agent",
    sub_agents=[parallel_analysis_agent, total_output_agent],
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=ROOT_AGENT_PROMPT,
    sub_agents=[greeter_agent, sequential_analysis_agent],
    before_agent_callback=_load_precreated_itinerary,
)
