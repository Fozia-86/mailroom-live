# check.py: tests for the subscriber functions in mailroom.py

from mailroom import read_subscribers, count_emails, count_group


# ========== tests ==========

subscribers: str = read_subscribers("data/subscribers.csv")

# Behavior 1: when the file is read, its output type is string
assert isinstance(subscribers, str), "reading the file should give back text (str)"

# Behavior 2: total number of emails is 24
assert count_emails(subscribers) == 24, "there should be 24 emails"

# Behavior 3: daily-drinkers group has 8 rows
assert count_group(subscribers, "daily-drinkers") == 8, "there should be 8 daily-drinkers"

print("All checks passed!")
