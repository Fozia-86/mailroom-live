# mailroom-live — a command-line mailroom management system
# Concepts used: variables & types (13.3), decisions (13.4),
# and/or & while (13.5), functions (13.6), lists & dicts (13.7)

# A type alias — gives a short name to a long type.
# MailItem is a dict where keys are str, values are str or int or bool.
type MailItem = dict[str, str | int | bool]


# ── Core functions ──────────────────────────────────────────


def make_item(item_id: int, recipient: str, item_type: str, description: str) -> MailItem:
    """Create a mail item dictionary."""
    item: MailItem = {
        "id": item_id,
        "recipient": recipient,
        "item_type": item_type,
        "description": description,
        "picked_up": False,
    }
    return item


def next_id(mailbox: list[MailItem]) -> int:
    """Return the next available ID (one more than the current count)."""
    return len(mailbox) + 1


def add_item(mailbox: list[MailItem], recipient: str, item_type: str, description: str) -> MailItem:
    """Create a new mail item and append it to the mailbox. Returns the item."""
    item_id: int = next_id(mailbox)
    item: MailItem = make_item(item_id, recipient, item_type, description)
    mailbox.append(item)
    return item


def find_item(mailbox: list[MailItem], item_id: int) -> MailItem | None:
    """Find an item by its ID. Returns the item dict, or None if not found."""
    for item in mailbox:
        if item["id"] == item_id:
            return item
    return None


def pick_up(mailbox: list[MailItem], item_id: int) -> bool:
    """Mark an item as picked up. Returns True if successful, False otherwise."""
    item: MailItem | None = find_item(mailbox, item_id)
    if item is None:
        return False
    if item["picked_up"]:
        return False
    item["picked_up"] = True
    return True


def pending_items(mailbox: list[MailItem]) -> list[MailItem]:
    """Return a list of items that have NOT been picked up yet."""
    result: list[MailItem] = []
    for item in mailbox:
        if not item["picked_up"]:
            result.append(item)
    return result


def count_by_type(mailbox: list[MailItem]) -> dict[str, int]:
    """Count how many items of each type are in the mailbox."""
    counts: dict[str, int] = {}
    for item in mailbox:
        item_type = str(item["item_type"])
        if item_type in counts:
            counts[item_type] = counts[item_type] + 1
        else:
            counts[item_type] = 1
    return counts


# ── Display helpers ─────────────────────────────────────────


def format_item(item: MailItem) -> str:
    """Format one mail item as a readable line."""
    status: str = "PICKED UP" if item["picked_up"] else "WAITING"
    return f"  [{item['id']}] {item['item_type']} for {item['recipient']} — {item['description']} ({status})"


def show_pending(mailbox: list[MailItem]) -> None:
    """Print all items waiting for pickup."""
    waiting: list[MailItem] = pending_items(mailbox)
    if len(waiting) == 0:
        print("\n  No items waiting for pickup.")
    else:
        print(f"\n  {len(waiting)} item(s) waiting:\n")
        for item in waiting:
            print(format_item(item))
    print()


def show_all(mailbox: list[MailItem]) -> None:
    """Print every item in the mailbox."""
    if len(mailbox) == 0:
        print("\n  Mailroom is empty.\n")
    else:
        print(f"\n  All items ({len(mailbox)} total):\n")
        for item in mailbox:
            print(format_item(item))
        print()


def show_stats(mailbox: list[MailItem]) -> None:
    """Print summary statistics."""
    total: int = len(mailbox)
    waiting: int = len(pending_items(mailbox))
    picked: int = total - waiting
    print(f"\n  Total items:   {total}")
    print(f"  Waiting:       {waiting}")
    print(f"  Picked up:     {picked}")
    if total > 0:
        counts: dict[str, int] = count_by_type(mailbox)
        print("  By type:")
        for item_type in sorted(counts):
            print(f"    {item_type}: {counts[item_type]}")
    print()


# ── Menu ────────────────────────────────────────────────────


MENU: str = """
========================================
        MAILROOM LIVE
========================================
  1. Log new item
  2. View pending pickups
  3. View all items
  4. Mark item as picked up
  5. Stats
  6. Quit
========================================
"""


def main() -> None:
    """Run the mailroom menu loop."""
    mailbox: list[MailItem] = []
    running: bool = True

    print("\nWelcome to Mailroom Live!")

    while running:
        print(MENU)
        choice: str = input("Choose an option (1-6): ").strip()

        if choice == "1":
            # Log a new item
            print()
            recipient: str = input("  Recipient name: ").strip()
            item_type: str = input("  Type (package / letter / parcel): ").strip().lower()
            description: str = input("  Description: ").strip()

            if recipient == "" or item_type == "" or description == "":
                print("\n  All fields are required. Item not added.")
            else:
                item: MailItem = add_item(mailbox, recipient, item_type, description)
                print(f"\n  Logged: {item['item_type']} for {item['recipient']} (ID: {item['id']})")

        elif choice == "2":
            show_pending(mailbox)

        elif choice == "3":
            show_all(mailbox)

        elif choice == "4":
            # Mark as picked up
            print()
            id_text: str = input("  Enter item ID to pick up: ").strip()
            if id_text == "":
                print("\n  No ID entered.")
            else:
                item_id: int = int(id_text)
                success: bool = pick_up(mailbox, item_id)
                if success:
                    print(f"\n  Item {item_id} marked as picked up.")
                else:
                    print(f"\n  Could not pick up item {item_id}. Check the ID and try again.")

        elif choice == "5":
            show_stats(mailbox)

        elif choice == "6":
            running = False
            print("\nGoodbye!\n")

        else:
            print("\n  Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
