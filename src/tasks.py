from dataclasses import dataclass, field
from crewai import Task

@dataclass
class TaskDefinition:
    description: str
    expected_output: str
    agent_role: str  # Role of the agent assigned to this task
    context_tasks: list = field(default_factory=list)

def get_tasks():
    triage_task = TaskDefinition(
        description="Classify incoming customer emails and route them to the appropriate department or agent.",
        expected_output="A classification of the email and the assigned department or agent.",
        agent_role="Customer Support Triage Agent",
    )

    response_task = TaskDefinition(
        description="Create accurate response drafts using information from the company's internal knowledge base.",
        expected_output="A draft response to the customer's email.",
        agent_role="Customer Support Response Agent",
    )

    review_task = TaskDefinition(
        description="Review and approve response drafts before they are sent to customers.",
        expected_output="Approval or feedback on the draft response.",
        agent_role="Customer Support Review Agent",
    )

    return [triage_task, response_task, review_task]

def create_task(definition: TaskDefinition, agent):
    return Task(
        description=definition.description,
        expected_output=definition.expected_output,
        agent=agent,
    )