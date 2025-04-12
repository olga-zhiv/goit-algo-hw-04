

def total_salary(path):   # задаємо функцію


    try:  
        with open(path, 'r', encoding='utf-8') as file:    # Відкриваємо файл для читання
            total = 0     # розрахунок загальної суми зарплат
            count = 0     # лічильник кількості робітників



            for line in file:    # Проходимо по кожному рядку у файлі
                line = line.strip()  # прибираємо зайві пробіли та переноси
                if line:  # якщо рядок не порожній


                    try:
                        name, salary = line.split(",")   # Розділяємо рядок на ім’я розробника та його зарплату
                        total += float(salary)    # Перетворюємо зарплату із строки в число
                        count += 1


                    except ValueError:
                        print(f"Неможливо обробити рядок: {line}")


            if count == 0:      # Якщо файл пустий повертаємо нулі
                return (0, 0)


            average = (total / count)   # Обчислюємо середню зарплату
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
            return (total, average)
    except FileNotFoundError:    # Обробка помилки, якщо файл не знайдено
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)


salary_total = total_salary("salary_file.txt")
print(salary_total)
