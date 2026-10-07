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
        description=(
            "Classify the customer email below."
            "First decide if it is relevant: a real message from a person about the Cinny app. "
            "Spam, phishing, newsletters, ads and messages unrelated to Cinny are SPAM."
            "If relevant, pick exactly one category:"
            "- ACCOUNT: login, password reset, deleting the account, sync between devices"
            "- BUG: crashes, lost watchlists or history, notifications not working, UI problems"
            "- DATA_ERROR: wrong or missing movie/series info, e.g. episodes, seasons, release dates, streaming services"
            "- FEEDBACK: feature requests, suggestions, praise or complaints about the app"
            "- OTHER: relevant to Cinny but fits none of the above"
            "Email:{email_content}"
        ),
        expected_output=(
            "Exactly three lines:"
            "CATEGORY: <SPAM | ACCOUNT | BUG | DATA_ERROR | FEEDBACK | OTHER>"
            "SUMMARY: <one sentence describing what the customer wants>"
            "REASON: <one sentence explaining the classification>"
        ),
        agent_role="Customer Support Triage Agent",
    )

    response_task = TaskDefinition(
        description=(
            "Write a reply to the customer email below, using the triage result from the previous task."
            "If the category is SPAM, do not write a reply; output only NO_REPLY."
            "Otherwise, write in friendly, casual English:"
            "- ACCOUNT: give the steps to fix it; never ask for their password"
            "- BUG: apologize, give any known workaround, and ask for device, OS and app version if missing"
            "- DATA_ERROR: thank them and say the title's info will be checked and corrected"
            "- FEEDBACK: thank them and say it is passed on to the product team; promise nothing"
            "- OTHER: answer as best you can, or say the team will get back to them"
            "Only use facts you know about Cinny. Do not invent features, prices or dates."
            "Email:{email_content}"
        ),
        expected_output="Either NO_REPLY, or a complete email draft with a greeting, a short body (max ~150 words) and the sign-off 'The Cinny Team'.",
        agent_role="Customer Support Response Agent",
    )

    review_task = TaskDefinition(
        description=(
            "Review the draft reply from the previous task against the customer email below."
            "If the draft is NO_REPLY, output NO_REPLY."
            "Otherwise, check that the draft:"
            "1. Answers everything the customer asked"
            "2. Contains no made-up facts, promises or dates"
            "3. Is in friendly, casual English and under ~150 words"
            "4. Never asks for passwords or payment details"
            "If it passes, keep it as is. If not, rewrite it so it does."
            "Email:{email_content}"
        ),
        expected_output="Either NO_REPLY, or only the final email text ready to send, with no comments or explanations.",
        agent_role="Customer Support Review Agent",
    )

    return [triage_task, response_task, review_task]

def create_task(definition: TaskDefinition, agent):
    return Task(
        description=definition.description,
        expected_output=definition.expected_output,
        agent=agent,
    )