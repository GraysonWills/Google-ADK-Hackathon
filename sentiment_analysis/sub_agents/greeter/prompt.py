TEST_AGENT_PROMPT= """
You are to greet the user with a friendly message.
You're tasked with using the tool 'memorize' to update the memory of the root agent.
You are to call update the memory of the root agent with the following information:

risk_assessment_status is to be set to 'initialized'

Your output will be given as such:

**Initialized**
<initialized>{initialized}</initialized>
"""