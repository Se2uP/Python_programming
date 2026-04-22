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

text = str(input("Введите вещественные числа: "))
print(find_max_float(text))