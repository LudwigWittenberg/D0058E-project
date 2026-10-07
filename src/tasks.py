from dataclasses import dataclass, field
from crewai import Task

@dataclass
class TaskDefinition:
    description: str
    expected_output: str
    agent_role: str  # Role of the agent assigned to this task
    context_tasks: list = field(default_factory=list)

# The customer email goes first and is clearly labelled, so small models don't
# mistake it for the text they are supposed to output
CUSTOMER_EMAIL = (
    "=== CUSTOMER EMAIL (input only, never copy it as your answer) ===\n"
    "{email_content}\n"
    "=== END OF CUSTOMER EMAIL ===\n\n"
)

def get_tasks():
    triage_task = TaskDefinition(
        description=(
            CUSTOMER_EMAIL
            + "Classify the customer email above.\n\n"
            "First decide if it is relevant: a real message from a person about the Cinny app. "
            "Spam, phishing, newsletters, ads and messages unrelated to Cinny are SPAM.\n\n"
            "If relevant, pick exactly one main category:\n"
            "- ACCOUNT: login, password reset, deleting the account, sync between devices\n"
            "- BUG: crashes, lost watchlists or history, notifications not working, UI problems\n"
            "- DATA_ERROR: wrong or missing movie/series info, e.g. episodes, seasons, release dates, streaming services\n"
            "- FEEDBACK: feature requests, suggestions, praise or complaints about the app\n"
            "- OTHER: relevant to Cinny but fits none of the above\n\n"
            "If the email contains more than one issue, list the rest under OTHER_ISSUES."
        ),
        expected_output=(
            "Exactly four lines:\n"
            "CATEGORY: <SPAM | ACCOUNT | BUG | DATA_ERROR | FEEDBACK | OTHER>\n"
            "SUMMARY: <one sentence describing what the customer wants>\n"
            "OTHER_ISSUES: <further issues with their category, or NONE>\n"
            "REASON: <one sentence explaining the classification>"
        ),
        agent_role="Customer Support Triage Agent",
    )

    response_task = TaskDefinition(
        description=(
            CUSTOMER_EMAIL
            + "You are The Cinny Team. Write a reply TO the customer who sent the email above, "
            "using the triage result from the previous task.\n\n"
            "If the category is SPAM, do not write a reply; output only NO_REPLY.\n\n"
            "Otherwise, address every issue (CATEGORY and OTHER_ISSUES) in friendly, casual English:\n"
            "- ACCOUNT: give the steps to fix it; never ask for their password\n"
            "- BUG: apologize and ask for device, OS and app version if missing\n"
            "- DATA_ERROR: thank them and say the title's info will be checked and corrected\n"
            "- FEEDBACK: thank them and say it is passed on to the product team; promise nothing\n"
            "- OTHER: answer as best you can, or say the team will get back to them\n\n"
            "Never describe menus, buttons or steps in the app unless you know they exist. "
            "Do not invent features, prices or dates."
        ),
        expected_output=(
            "Either NO_REPLY, or a reply email to the customer: a greeting using their name, "
            "a short body (max ~150 words) and the sign-off 'The Cinny Team'."
        ),
        agent_role="Customer Support Response Agent",
    )

    review_task = TaskDefinition(
        description=(
            CUSTOMER_EMAIL
            + "The previous task wrote a draft reply from The Cinny Team to this customer. "
            "Review that DRAFT REPLY, not the customer email.\n\n"
            "If the draft is NO_REPLY, output NO_REPLY.\n\n"
            "Otherwise, check that the draft:\n"
            "1. Is written to the customer and signed 'The Cinny Team'\n"
            "2. Answers every issue the customer raised\n"
            "3. Contains no made-up facts, app steps, promises or dates\n"
            "4. Is in friendly, casual English and under ~150 words\n"
            "5. Never asks for passwords or payment details\n\n"
            "If it passes, keep it as is. If not, rewrite it so it does."
        ),
        expected_output=(
            "Either NO_REPLY, or only the final reply email from The Cinny Team to the customer, "
            "ready to send, with no comments or explanations. Never the customer's own email."
        ),
        agent_role="Customer Support Review Agent",
    )

    return [triage_task, response_task, review_task]

def create_task(definition: TaskDefinition, agent):
    return Task(
        description=definition.description,
        expected_output=definition.expected_output,
        agent=agent,
    )
