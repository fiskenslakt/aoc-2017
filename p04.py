from collections import Counter

from aocd import data


def no_duplicates(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def no_anagrams(passphrase):
    words = passphrase.split()
    letter_frequencies = set()

    for word in words:
        letter_frequencies.add(
            tuple(sorted(Counter(word).items()))
        )

    return len(words) == len(letter_frequencies)


no_dups = 0
no_grams = 0

for passphrase in data.splitlines():
    if no_duplicates(passphrase):
        no_dups += 1

for passphrase in data.splitlines():
    if no_anagrams(passphrase):
        no_grams += 1

print('Part 1:', no_dups)
print('Part 2:', no_grams)
