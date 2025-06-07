from google.adk.agents import Agent, ParallelAgent, SequentialAgent

from sentiment_analysis.sub_agents.audio.prompt import (
    AUDIO_SPEED_AGENT_PROMPT,
    AUDIO_PITCH_AGENT_PROMPT,
    AUDIO_TRANSCRIPT_AGENT_PROMPT,
    AUDIO_OUTPUT_AGENT_PROMPT,
)
from sentiment_analysis.tools.load import memorize

audio_speed_agent = Agent(
    model="gemini-2.0-flash",
    name="audio_speed_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=AUDIO_SPEED_AGENT_PROMPT,
    tools=[memorize],
)

audio_pitch_agent = Agent(
    model="gemini-2.0-flash",
    name="audio_pitch_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=AUDIO_PITCH_AGENT_PROMPT,
    tools=[memorize],
)

audio_transcript_agent = Agent(
    model="gemini-2.0-flash",
    name="audio_transcript_agent",
    description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
    instruction=AUDIO_TRANSCRIPT_AGENT_PROMPT,
    tools=[memorize],
)

# parallel_audio_analysis_agent = ParallelAgent(
#     name="parallel_audio_agent",
#     sub_agents=[audio_speed_agent, audio_pitch_agent, audio_transcript_agent],
# )

# audio_output_agent = Agent(
#     model="gemini-2.0-flash",
#     name="audio_output_agent",
#     description="a sentiment analysis agent that analyzes audio recordings for emotional tone and content",
#     instruction=AUDIO_OUTPUT_AGENT_PROMPT,
#     tools=[memorize],
# )

# audio_pipeline_agent = SequentialAgent(
#     name="audio_pipeline_agent",
#     sub_agents=[parallel_audio_analysis_agent, audio_output_agent],
# )