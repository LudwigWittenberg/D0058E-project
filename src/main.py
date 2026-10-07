from crew import create_crew

from test_emails import TEST_EMAILS

def main():
    crew = create_crew()

    for expected, email in TEST_EMAILS:
        result = crew.kickoff(inputs={"email_content": email})
        triage = result.tasks_output[0].raw.strip()
        print(f"\n{'=' * 70}\nEXPECTED: {expected}\n\n--- EMAIL ---\n{email}")
        print(f"\n--- TRIAGE ---\n{triage}\n\n--- FINAL REPLY ---\n{result.raw}")

    # result = crew.kickoff(inputs=TEST_EMAILS)
    # print("\n===== FINAL REPLY =====\n")
    # print(result.raw)


if __name__ == "__main__":
    main()
