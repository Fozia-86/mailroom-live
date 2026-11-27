"""Mailroom subscriber functions — real implementations."""
import sys


def read_subscribers(path: str) -> str:
    """Read the whole file at 'path' and return it as one piece of text."""
    with open(path, encoding="utf-8") as f:
        text: str = f.read()
    return text


def count_emails(text: str) -> int:
    """Count the subscriber rows (one email per row, header not counted)."""
    count: int = 0
    for line in text.splitlines():
        if line:
            count += 1
    count -= 1
    return count


def count_group(text: str, group: str) -> int:
    """Count the rows whose group column equals 'group'."""
    lines = text.splitlines()
    data_lines = lines[1:]
    count = 0
    for line in data_lines:
        columns = line.split(",")
        if columns[3] == group:
            count += 1
    return count


# Front door: only runs for `uv run mailroom.py <name>`, not when imported
if __name__ == "__main__":
    name: str = sys.argv[1]  # e.g. "subscribers"
    text: str = read_subscribers("data/" + name + ".csv")

    print(count_emails(text), "emails")
    groups: list[str] = ["daily-drinkers", "gift-buyers", "tea-curious"]
    for group in groups:
        print(group + ":", count_group(text, group))
