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

text = str(input("Введите числа: "))
print(max_consecutive_digits(text))