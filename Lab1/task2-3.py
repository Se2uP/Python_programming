def count_russian_letters(text: str) -> int:
    count = 0
    for char in text:
        if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            count += 1
    return count

def is_latin_palindrome(text: str) -> bool:
    filtered = ""

    for char in text:
        if 'a' <= char <= 'z':  # только строчные латинские
            filtered += char

    return filtered == filtered[::-1]

def find_dates(text: str) -> list:
    import re
    pattern = r'\d{2}\.\d{2}\.\d{4}'
    return re.findall(pattern, text)

def main():
    print("Выбери задачу:")
    print("1 — Посчитать русские символы")
    print("2 — Проверить палиндром (латиница)")
    print("3 — Найти даты")

    choice = input("Твой выбор: ")

    text = input("Введи строку: ")

    if choice == "1":
        result = count_russian_letters(text)
        print("Количество русских символов:", result)

    elif choice == "2":
        result = is_latin_palindrome(text)
        print("Палиндром:", result)

    elif choice == "3":
        result = find_dates(text)
        print("Найденные даты:", result)

    else:
        print("Ты что-то не то ввёл")

if __name__ == "__main__":
    main()