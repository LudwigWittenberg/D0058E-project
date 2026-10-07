from agents import create_agent, get_agents

def main():
    agents = get_agents()
    for agent_def in agents:
        agent = create_agent(agent_def)
        print(f"Created agent: {agent.role} with goal: {agent.goal}")


if __name__ == "__main__":
    main()
