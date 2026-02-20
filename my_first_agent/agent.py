from google.adk.agents import Agent

root_agent = Agent(
    name="root_agent",
    description="This is the root agent for my first agent.",
    instruction="You are the root agent. You are a helpful ai assistant to provide clear and concise answers to the user queries",
    tools=[],
    model="gemini-2.0-flash",
)