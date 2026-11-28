# mailroom.py: tools for working with the subscribers file

import sys
from datetime import date, timedelta


def read_subscribers(path: str) -> str:
    """Promise: give back the whole file at `path` as one piece of text."""
    with open(path, encoding="utf-8") as f:
        text: str = f.read()
    return text


def count_emails(text: str) -> int:
    """Promise: count the subscriber rows (one email per row, header not counted)."""
    count: int = 0
    for line in text.splitlines():
        if line:  # skip empty lines ("" counts as "no")
            count += 1
    return count - 1  # the first line is the header, not an email


def count_group(text: str, group: str) -> int:
    """Promise: count the rows whose group column equals `group`."""
    count: int = 0
    for line in text.splitlines():
        columns: list[str] = line.split(",")
        if columns[3] == group:  # column 3 is "group"
            count += 1
    return count


def count_consent(text: str) -> int:
    """Promise: count the subscriber rows whose consent column is not empty (header not counted)."""
    count: int = 0
    for line in text.splitlines():
        columns: list[str] = line.split(",")
        if line and columns[5]:  # column 5 is "consent"; "" counts as "no"
            count += 1
    return count - 1  # the header's consent column says "consent", so it was counted once


def count_joined_since(text: str, run_date: str, days: int) -> int:
    """Promise: count the rows that joined from `days` days before `run_date` up to `run_date`, both ends counted."""
    run: date = date.fromisoformat(run_date)
    cutoff: date = run - timedelta(days=days)  # 2026-11-20 - 30 days = 2026-10-21
    count: int = 0
    for line in text.splitlines():
        columns: list[str] = line.split(",")
        if line and not columns[4] == "joined_on":  # column 4 is "joined_on"; skip the header
            joined: date = date.fromisoformat(columns[4])
            if cutoff <= joined and joined <= run:
                count += 1
    return count


def next_send(run_date: str) -> str:
    """Promise: give back the first Monday of the month after `run_date`, as year-first text."""
    run: date = date.fromisoformat(run_date)
    year: int = run.year
    month: int = run.month + 1
    if month == 13:  # December rolls over to January of the next year
        month = 1
        year += 1
    day: date = date(year, month, 1)
    while not day.weekday() == 0:  # 0 is Monday
        day = day + timedelta(days=1)
    return day.isoformat()


# Front door: only runs for `uv run mailroom.py <command>`, not when imported
if __name__ == "__main__":
    command: str = sys.argv[1]  # "subscribers" or "next-send"

    # Read the optional words: --run-date 2026-11-20 and --since-days 30
    run_date: str = ""
    since_days: str = ""
    previous: str = ""
    for word in sys.argv:
        if previous == "--run-date":
            run_date = word
        if previous == "--since-days":
            since_days = word
        previous = word

    # The ONLY place today's date is read, and only when --run-date was left out
    run_date = run_date or date.today().isoformat()

    # Each command is checked by name, so an unknown command runs nothing
    if command == "next-send":
        print("next send:", next_send(run_date))
    if command == "subscribers":
        text: str = read_subscribers("data/subscribers.csv")
        print(count_emails(text), "emails")
        groups: list[str] = ["daily-drinkers", "gift-buyers", "tea-curious"]
        for group in groups:
            print(group + ":", count_group(text, group))
        print("consent:", count_consent(text))
        if since_days:
            days: int = int(since_days)
            print(count_joined_since(text, run_date, days), "joined in the last", days, "days")
