from crew import create_crew

from test_emails import TEST_EMAILS

TEST_EMAIL = {"email_content": """Subject: A few questions before I upgrade

Hi Cinny team,

I'm thinking about upgrading to Cinny Plus. How much does it cost, and can I cancel anytime?

Also, before I do: is there a way to export my watch history? I've tracked over 300 movies
and I don't want to lose them. And if I end up deleting my account, how long until my data
is actually gone?

Thanks!
Nora"""}

def main():
    crew = create_crew()

    # for expected, email in TEST_EMAILS:
    #     result = crew.kickoff(inputs={"email_content": email})
    #     triage = result.tasks_output[0].raw.strip()
    #     print(f"\n{'=' * 70}\nEXPECTED: {expected}\n\n--- EMAIL ---\n{email}")
    #     print(f"\n--- TRIAGE ---\n{triage}\n\n--- FINAL REPLY ---\n{result.raw}")

    result = crew.kickoff(inputs=TEST_EMAIL)
    print("\n===== FINAL REPLY =====\n")
    print(result.raw)


if __name__ == "__main__":
    main()
