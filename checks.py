# checks.py: tests for the tools in mailroom.py

from mailroom import read_subscribers, count_emails, count_group, count_consent
from mailroom import count_joined_since, next_send

subscribers: str = read_subscribers("data/subscribers.csv")

# Behavior 1: when the file is read, its output type is string
assert isinstance(subscribers, str), "reading the file should give back text (str)"

# Behavior 2: total number of emails is 24
assert count_emails(subscribers) == 24, "there should be 24 emails"

# Behavior 3: the daily-drinkers group has 8 rows
assert count_group(subscribers, "daily-drinkers") == 8, "daily-drinkers should have 8 rows"

# Behavior 5: 24 subscribers gave consent (consent column is not empty)
assert count_consent(subscribers) == 24, "there should be 24 subscribers with consent"

# Behavior 6: with run date 2026-11-20, 7 subscribers joined in the last 30 days
assert count_joined_since(subscribers, "2026-11-20", 30) == 7, "7 should have joined in the last 30 days"

# Behavior 7: the edge day counts. 2026-11-20 minus 30 days is 2026-10-21 (inclusive)
edge: str = "first_name,last_name,email,group,joined_on,consent\nSam,Lee,sam@example.com,tea-curious,2026-10-21,waitlist form\n"
assert count_joined_since(edge, "2026-11-20", 30) == 1, "a join on 2026-10-21 should count"

# Behavior 8: the next send is the first Monday of the next month
assert next_send("2026-11-20") == "2026-12-07", "after 2026-11-20 the next send is 2026-12-07"
assert next_send("2026-12-07") == "2027-01-04", "after 2026-12-07 the next send is 2027-01-04 (year end)"

print("all checks passed")

# Behavior 4 (written before the code, checked by hand for now):
# `uv run mailroom.py subscribers` reads data/subscribers.csv and prints exactly:
#
#   24 emails
#   daily-drinkers: 8
#   gift-buyers: 8
#   tea-curious: 8
#   consent: 24
#
# `uv run mailroom.py subscribers --since-days 30 --run-date 2026-11-20` prints
# the same 5 lines, then ends with:
#
#   7 joined in the last 30 days
#
# `uv run mailroom.py next-send --run-date 2026-11-20` prints exactly:
#
#   next send: 2026-12-07
#
# Leaving out --run-date uses today's date. Today's date is read only in the
# front door of mailroom.py, never inside the logic.
