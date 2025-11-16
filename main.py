from storage import save_data, load_data
from address_book import AddressBook
from record import Record
from fields import Name, Phone


def parse_input(user_input: str):
    """
    Розбиває введення користувача на команду та аргументи.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


# ------------------------ COMMAND HANDLERS ------------------------

def handle_add(args, book: AddressBook):
    """
    Додає новий контакт.
    Формат: add Name Phone
    """
    if len(args) != 2:
        return "Usage: add Name Phone"

    name, phone = args
    if book.get(name):
        return f"Error: Contact '{name}' already exists."

    try:
        record = Record(Name(name))
        record.add_phone(Phone(phone))
    except ValueError as e:
        return f"Error: {e}"

    book.add_record(record)
    return f"Contact '{name}' added successfully."


def handle_change(args, book: AddressBook):
    """
    Змінює телефон контакту.
    Формат: change Name NewPhone
    """
    if len(args) != 2:
        return "Usage: change Name NewPhone"

    name, new_phone = args
    record = book.get(name)

    if not record:
        return f"Error: Contact '{name}' not found."

    if not record.phones:
        return "Error: This contact has no phones to change."

    old_phone = record.phones[0].value

    try:
        Phone(new_phone)  # валідація
    except ValueError as e:
        return f"Error: {e}"

    record.edit_phone(old_phone, new_phone)
    return f"Phone for '{name}' updated successfully."


def handle_phone(args, book: AddressBook):
    """
    Показує телефони контакту.
    Формат: phone Name
    """
    if len(args) != 1:
        return "Usage: phone Name"

    name = args[0]
    record = book.get(name)

    if not record:
        return f"Error: Contact '{name}' not found."

    phones = ", ".join([p.value for p in record.phones])
    return f"{name}: {phones}"


def handle_show_all(book: AddressBook):
    """
    Показує всі контакти.
    """
    if not book.data:
        return "AddressBook is empty."

    result = []
    for name, record in book.data.items():
        phones = ", ".join([p.value for p in record.phones])
        result.append(f"{name}: {phones}")

    return "\n".join(result)


# ------------------------ MAIN PROGRAM ------------------------

def main():
    print("Loading AddressBook...")
    book: AddressBook = load_data()
    print(f"Loaded {len(book.data)} contact(s).")

    while True:
        try:
            user_input = input("Enter command: ")
        except KeyboardInterrupt:
            print("\nForce exit. Saving data...")
            save_data(book)
            break

        cmd, args = parse_input(user_input)

        if not cmd:
            print("Please enter a command.")
            continue

        # вихід
        if cmd in ("exit", "close", "quit"):
            print("Saving data...")
            save_data(book)
            print("Goodbye!")
            break

        # команди
        elif cmd == "add":
            print(handle_add(args, book))

        elif cmd == "change":
            print(handle_change(args, book))

        elif cmd == "phone":
            print(handle_phone(args, book))

        elif cmd == "all":
            print(handle_show_all(book))

        # невідома команда
        else:
            print("Unknown command. Available commands: add, change, phone, all, exit")


if __name__ == "__main__":
    main()
