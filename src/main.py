from crew import create_crew

email = {"email_content": """Subject: My watchlist is gone

Hi,

I updated Cinny yesterday and now my whole watchlist is empty. I had like 40 shows in there.
Also, the app keeps saying the new season of Severance isn't out yet, but it's already streaming.
Can you help?

Thanks,
Alex"""}

def main():
    crew = create_crew()

    result = crew.kickoff(inputs=email)
    print("\n===== FINAL REPLY =====\n")
    print(result.raw)


if __name__ == "__main__":
    main()
