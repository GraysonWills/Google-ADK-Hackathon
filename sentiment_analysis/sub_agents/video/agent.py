from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from sentiment_analysis.sub_agents.video.prompt import VIDEO_OUTPUT_AGENT_PROMPT, FACIAL_ANALYSIS_AGENT_PROMPT, BODY_POSTURE_AGENT_PROMPT
from sentiment_analysis.tools.load import memorize

facial_analysis_agent = Agent(
    model="gemini-2.0-flash",
    name="facial_analysis_agent",
    description="You are a facial analysis agent that analyzes the facial expressions of the people in a video recording.",
    instruction=FACIAL_ANALYSIS_AGENT_PROMPT,
    tools=[memorize],
)

body_posture_agent = Agent(
    model="gemini-2.0-flash",
    name="body_posture_agent",
    description="You are a body posture agent that analyzes the body posture of the people in a video recording.",
    instruction=BODY_POSTURE_AGENT_PROMPT,
    tools=[memorize],
)

parallel_video_analysis_agent = ParallelAgent(
    name="parallel_video_agent",
    sub_agents=[facial_analysis_agent, body_posture_agent],
)

video_output_agent = Agent(
    model="gemini-2.0-flash",
    name="video_output_agent",
    description="You are a video output agent that analyzes the facial expressions and body posture of the people in a video recording.",
    instruction=VIDEO_OUTPUT_AGENT_PROMPT,
    tools=[memorize],
)

video_pipeline_agent = SequentialAgent(
    name="video_pipeline_agent",
    sub_agents=[parallel_video_analysis_agent, video_output_agent],
)