def parse_input(user_input):
    # Розбиваємо рядок користувача на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # перетворюємо команду на нижній регістр
    return cmd, args


# Додає новий контакт
def add_contact(args, contacts):
    # Перевіряємо, чи передано два аргументи: ім’я та номер
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone  # додаємо до словника
    return "Contact added."


# Змінює існуючий номер телефону
def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone  # оновлюємо номер
        return "Contact updated."
    else:
        return "Contact not found."  # якщо ім’я не знайдено


# Показує номер телефону за ім’ям
def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")  # повертаємо номер або повідомлення
    

# Показує всі збережені контакти
def show_all(args, contacts):
    if args:
        return "Usage: all"  # команда "all" не повинна мати аргументів
    if not contacts:
        return "No contacts saved."
    # Формуємо рядок з усіма контактами
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


# Основна функція — логіка роботи бота
def main():
    contacts = {}  # Порожній словник для зберігання контактів
    print("Welcome to the assistant bot!")

    # Словник команд і відповідних їм функцій
    handlers = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    while True:
        user_input = input("Enter a command: ")  # Запитуємо команду в користувача
        command, args = parse_input(user_input)  # Розбираємо її

        # Обробляємо команди виходу
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Привітальна команда
        elif command == "hello":
            print("How can I help you?")

        # Якщо команда є серед обробників — викликаємо відповідну функцію
        elif command in handlers:
            handler = handlers[command]
            print(handler(args, contacts))  # передаємо аргументи і словник контактів

        # Якщо команда не відома
        else:
            print("Invalid command.")

# Точка входу — запуск програми
if __name__ == "__main__":
    main()
