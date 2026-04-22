def sort_by_word_count(strings: list) -> list:
    return sorted(strings, key=lambda s: len(s.split()))


def main():
    n = int(input("Сколько строк? "))
    strings = []

    for _ in range(n):
        strings.append(input())

    result = sort_by_word_count(strings)

    print("Результат:")
    for s in result:
        print(s)


if __name__ == "__main__":
    main()