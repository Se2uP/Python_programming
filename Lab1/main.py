def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def sum_of_prime_divisors(number: int) -> int:
    if number == 0:
        raise ValueError("For zero, prime divisors are undefined.")

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


if __name__ == "__main__":
    number = int(input("Enter number: "))
    print(sum_of_prime_divisors(number))
