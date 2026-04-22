import re
def find_text_dates(text: str) -> list:
    pattern = r'\b\d{1,2}\s+(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+\d{4}\b'

    result = []
    pos = 0

    while True:
        match = re.search(pattern, text[pos:])
        if not match:
            break

        result.append(match.group())
        pos += match.end()

    return result

text = str(input("Введите текст: "))
print(find_text_dates(text))