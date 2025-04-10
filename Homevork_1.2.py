

def get_cats_info(path):
    cats = []  # створюємо порожній список для збереження словників
    try:
        with open(path, 'r', encoding='utf-8') as file:    # Відкриваємо файл у режимі читання
            for line in file:
                line = line.strip()  # прибираємо зайві пробіли та символи переносу
                if line:  # перевіряємо, що рядок не порожній
                    parts = line.split(",")  # розбиваємо рядок на частини за комою
                    if len(parts) == 3:
                        cat_id, name, age = parts  # розпаковуємо дані
                        cats.append({
                            "id": cat_id,
                            "name": name,
                            "age": age
                        })
                    else:
                        print(f"Неправильний формат рядка: {line}")
        return cats

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)