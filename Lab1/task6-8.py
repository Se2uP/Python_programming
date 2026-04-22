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

text = str(input("Введите дробные числа: "))
print(find_min_rational(text))