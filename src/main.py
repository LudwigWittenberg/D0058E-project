from crew import create_crew

from test_emails import TEST_EMAILS

import sys, time

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

    # result = crew.kickoff(inputs=TEST_EMAIL)
    # print("\n===== FINAL REPLY =====\n")
    # print(result.raw)

    start = time.perf_counter()
    result = crew.kickoff(inputs=TEST_EMAIL)
    print(result.raw)
    print(f"Time: {time.perf_counter() - start:.0f} s")
    print(f"LLM requests: {result.token_usage.successful_requests}")
    print(f"Tokens: {result.token_usage.total_tokens}")


if __name__ == "__main__":
    main()
