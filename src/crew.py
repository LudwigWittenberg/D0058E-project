from agents import create_agent, get_agents
from tasks import create_task, get_tasks
from crewai import Agent, Crew, Process, LLM

# llama3.2:3b writes the delegation tool call as plain text instead of calling it,
# so the manager runs on a larger model that handles tool calling
manager_llm = LLM(
  model="openai/qwen2.5:3b",
  base_url="http://localhost:11434/v1",
  api_key="ollama",
)

def create_manager():
  # Delegated coworkers only see the task and context the manager writes, not our
  # task descriptions, so the manager must pass the customer email on explicitly
  return Agent(
    role="Customer Support Manager",
    goal="Get every customer email classified, answered and reviewed by the right coworker.",
    backstory=(
      "You manage the Cinny support team. You never answer customers yourself. "
      "You always delegate in this order: Customer Support Triage Agent, then "
      "Customer Support Response Agent, then Customer Support Review Agent. "
      "When you delegate, ALWAYS copy the full customer email into the context field, "
      "together with the results from the previous coworkers."
    ),
    llm=manager_llm,
    allow_delegation=True,
  )

def create_crew():
  agents = get_agents()
  tasks = get_tasks()

  for i in range(len(agents)):
    agent = create_agent(agents[i])
    task = create_task(tasks[i], agent)

    # print(f"Assigned task: {task.description} to agent: {agent.role}")

    agents[i] = agent
    tasks[i] = task

  # The manager agent must not be in the agents list
  return Crew(
      agents=agents,
      tasks=tasks,
      process=Process.hierarchical,
      manager_agent=create_manager(),
  )
