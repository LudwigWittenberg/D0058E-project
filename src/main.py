from crew import create_crew

email = {"email_content": "Buy the crafter!"}

def main():
    crew = create_crew()

    crew.kickoff(inputs=email)


if __name__ == "__main__":
    main()
