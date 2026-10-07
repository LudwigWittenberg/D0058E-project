from agents import create_agent, get_agents
from tasks import create_task, get_tasks
from crewai import Crew

def create_crew():
  agents = get_agents()
  tasks = get_tasks()
  
  for i in range(len(agents)):
    agent = create_agent(agents[i])
    task = create_task(tasks[i], agent)

    # print(f"Assigned task: {task.description} to agent: {agent.role}")

    agents[i] = agent
    tasks[i] = task

  return Crew(
      agents=agents,
      tasks=tasks
  )