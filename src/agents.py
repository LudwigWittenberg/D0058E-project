import os
from crewai import Agent,
from dataclasses import dataclass, field
from llm import llm

# Definition schema
@dataclass
class agent_definition:
    role: str
    goal: str
    backstory: str
    tools: list = field(default_factory=list)
    allow_delegation: bool = False
    verbose: bool = True

# Create definitions of the agents
def get_agents():
  triage_agent = agent_definition(
    role="Customer Support Triage Agent",
    goal="Classify incomming customer emails and route them to the appropriate department or agent.",
    backstory="You are an experienced customer support coordinator responsible for routing support cases correctly."
  )

  response_agent = agent_definition(
    role="Customer Support Response Agent",
    goal="Create accurate response drafts using information from the company's internal knowledge base.",
    backstory="You are an experienced support specialist who relies on official company documentation before answering customer questions."
    # TODO: Add RAG
  )

  review_agent = agent_definition(
    role="Customer Support Review Agent",
    goal="Review and approve response drafts before they are sent to customers.",
    backstory="You are an experienced customer support manager responsible for ensuring the quality and accuracy of all customer communications."
  )

  return [triage_agent, response_agent, review_agent]


def create_agent(definition: agent_definition):
    return Agent(
        role=definition.role,
        goal=definition.goal,
        backstory=definition.backstory,
        tools=definition.tools,
        allow_delegation=definition.allow_delegation,
        verbose=definition.verbose,
        llm=llm,
    )