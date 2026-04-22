def sort_by_length(strings: list) -> list:
    return sorted(strings, key=len)


def main():
    n = int(input("Сколько строк? "))
    strings = []

    for _ in range(n):
        s = input()
        strings.append(s)

    sorted_strings = sort_by_length(strings)

    print("Результат:")
    for s in sorted_strings:
        print(s)


if __name__ == "__main__":
    main()