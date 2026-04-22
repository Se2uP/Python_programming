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


def count_odd_digits_greater_than_three(number: int) -> int:
    count = 0

    for digit in str(abs(number)):
        digit_value = int(digit)
        if digit_value % 2 == 1 and digit_value > 3:
            count += 1

    return count


def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))


def product_of_divisors_with_smaller_digit_sum(number: int) -> int:
    if number == 0:
        raise ValueError("Для числа 0 делители не определены.")

    product = 1
    source_digit_sum = digit_sum(number)

    for divisor in range(1, abs(number) + 1):
        if number % divisor == 0 and digit_sum(divisor) < source_digit_sum:
            product *= divisor

    return product


if __name__ == "__main__":
    number = int(input("Введите число: "))
    print(sum_of_prime_divisors(number))
