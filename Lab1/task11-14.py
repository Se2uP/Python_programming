def count_vowels_and_consonants_diff(s: str) -> int:
    vowels = "aeiouyаеёиоуыэюя"
    v = 0
    c = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1

    return abs(c - v)


def sort_by_vowel_consonant_diff(strings: list) -> list:
    return sorted(strings, key=count_vowels_and_consonants_diff)

def avg_ascii(s: str) -> float:
    if len(s) == 0:
        return 0
    return sum(ord(ch) for ch in s) / len(s)


def sort_by_ascii_deviation(strings: list) -> list:
    first_avg = avg_ascii(strings[0])
    return sorted(strings, key=lambda s: abs(avg_ascii(s) - first_avg))

n = int(input("Сколько строк? "))
strings = [input() for _ in range(n)]
print(sort_by_ascii_deviation(strings))