def find_max_float(text: str) -> float:
    numbers = text.split()
    max_num = float('-inf')

    for item in numbers:
        try:
            num = float(item)
            if num > max_num:
                max_num = num
        except:
            continue

    return max_num

def find_min_rational(text: str) -> float:
    numbers = text.split()
    min_num = float('inf')

    for item in numbers:
        if '/' in item:
            try:
                num = float(item.split('/')[0]) / float(item.split('/')[1])
                if num < min_num:
                    min_num = num
            except:
                continue

    return min_num

def max_consecutive_digits(text: str) -> int:
    max_count = 0
    current = 0

    for char in text:
        if char.isdigit():
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0

    return max_count

def main():
    print("Выбери задачу:")
    print("1 — Максимальное вещественное число")
    print("2 — Минимальное рациональное число")
    print("3 — Максимум подряд идущих цифр")

    choice = input("Твой выбор: ")
    text = input("Введи строку: ")

    if choice == "1":
        print(find_max_float(text))
    elif choice == "2":
        print(find_min_rational(text))
    elif choice == "3":
        print(max_consecutive_digits(text))
    else:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()