import csv

# Функция для создания телефонного справочника
def create_phonebook(filename):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Номер", "Комментарий"])
        writer.writerow(["Иван Иванов", "+7 (123) 456-7890", "Друг"])
        writer.writerow(["Петр Петров", "+7 (234) 567-8901", "Коллега"])
        writer.writerow(["Мария Сидорова", "+7 (345) 678-9012", "Мама"])
        writer.writerow(["Анна Кузнецова", "+7 (456) 789-0123", "Сестра"])
        writer.writerow(["Сергей Новиков", "+7 (567) 890-1234", "Отец"])
    print(f"Создан телефонный справочник '{filename}'.")

# Функция для копирования данных из одного файла в другой по номеру строки
def copy_entry(source_filename, destination_filename, line_number):
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file)
            lines = list(reader)
            if 1 <= line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(destination_filename, 'a', encoding='utf-8', newline='') as dest_file:
                    writer = csv.writer(dest_file)
                    writer.writerow(line_to_copy)
                print(f"Строка {line_number} скопирована из {source_filename} в {destination_filename}.")
            else:
                print(f"Строки с номером {line_number} нет в файле {source_filename}.")
    except FileNotFoundError:
        print("Файл не найден.")

# Пример использования функций
if __name__ == "__main__":
    phonebook_filename = "phonebook.csv"
    create_phonebook(phonebook_filename)
    
    source_filename = "source.csv"
    with open(source_filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Номер", "Комментарий"])
        writer.writerow(["Екатерина Крылова", "+7 (678) 901-2345", "Друг"])
        writer.writerow(["Алексей Смирнов", "+7 (789) 012-3456", "Коллега"])
        writer.writerow(["Марина Иванова", "+7 (890) 123-4567", "Мама"])
        writer.writerow(["Андрей Петров", "+7 (901) 234-5678", "Брат"])
        writer.writerow(["Ольга Николаева", "+7 (012) 345-6789", "Коллега"])
    
    destination_filename = "destination.csv"
    
    # Пользователь вводит номер строки для копирования
    line_number_to_copy = int(input("Введите номер строки для копирования из source.csv в destination.csv: "))
    copy_entry(source_filename, destination_filename, line_number_to_copy)