def count_russian_letters(text: str) -> int:
    count = 0
    for char in text:
        if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            count += 1
    return count

if __name__ == "__main__":
    text = str(input("Введите текст на русском языке: "))
    print(count_russian_letters(text))