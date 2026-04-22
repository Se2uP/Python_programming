def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True

def sum_of_prime_divisors(number: int) -> int:
    if number == 0:
        raise ValueError("Для числа 0 простые делители не определены.")

    total = 0

    for divisor in range(2, abs(number) + 1):
        if number % divisor == 0 and is_prime(divisor):
            total += divisor

    return total

number = int(input("Введите число: "))
print(sum_of_prime_divisors(number))