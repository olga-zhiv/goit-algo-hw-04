def parse_input(user_input):
    # Розбиваємо рядок користувача на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # перетворюємо команду на нижній регістр
    return cmd, args


# Додає новий контакт до словника
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Змінює існуючий номер телефону для імені
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


# Показує номер телефону за іменем
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


# Виводить всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print("Usage: add [name] [phone]")

        elif command == "change":
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print("Usage: change [name] [new_phone]")

        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print("Usage: phone [name]")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


# Точка входу у програму
if __name__ == "__main__":
    main()

