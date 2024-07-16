def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Format: add [name] [phone]"


def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name not in contacts:
            return "Contact with such name does not exist"
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Invalid command. Format: change [name] [phone]"


def show_phone(args, contacts):
    if len(args) == 1 and args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact not found."


def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, args = parse_input(user_input)
        else:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")


main()
