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

n = int(input("Сколько строк? "))
strings = [input() for _ in range(n)]
print(sort_by_vowel_consonant_diff(strings))