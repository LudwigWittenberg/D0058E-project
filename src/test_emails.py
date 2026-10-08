# Test emails with the category we expect triage to pick
TEST_EMAILS = [
    ("SPAM", """Subject: Buy the crafter!

Limited offer!!! Get the new Crafter 3000 for only $9.99. Click here: http://cheap-crafter.biz"""),

    ("SPAM", """Subject: Your Cinny account will be suspended

Dear user, we detected unusual activity. Verify your password and credit card within 24 hours
at http://cinny-secure-login.ru or your account will be deleted."""),

    ("ACCOUNT", """Subject: Can't log in

Hi, I forgot my password and the reset email never shows up, I've checked spam too.
My account email is sam@example.com. Please help!
Sam"""),

    ("BUG", """Subject: App crashes on start

Hey, since this morning Cinny crashes every time I open it. iPhone 13, iOS 18.1, latest app version.
I've already tried reinstalling it.
/Maria"""),

    ("DATA_ERROR", """Subject: Wrong episode count

Hi! The Bear season 3 shows 8 episodes in Cinny but it actually has 10, so I can't mark the last two as watched.
Thanks, Jonas"""),

    ("FEEDBACK", """Subject: Feature idea

Love the app! Would be amazing if I could share my watchlist with my girlfriend so we can pick
something to watch together. Any plans for that?
Cheers, Tom"""),

    ("OTHER", """Subject: Question

Hi, is Cinny available on Android TV? Couldn't find it in the Play Store on my TV.
Lisa"""),

    ("BUG + DATA_ERROR", """Subject: My watchlist is gone

Hi,

I updated Cinny yesterday and now my whole watchlist is empty. I had like 40 shows in there.
Also, the app keeps saying the new season of Severance isn't out yet, but it's already streaming.
Can you help?

Thanks,
Alex"""),

    ("ACCOUNT (Swedish)", """Ämne: Radera mitt konto

Hej, jag vill att ni raderar mitt konto och all min data. Hur gör jag det?
Mvh Erik"""),
]
