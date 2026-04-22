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

if __name__ == "__main__":
    text = str(input("Введите текст: "))
    print(is_latin_palindrome(text))