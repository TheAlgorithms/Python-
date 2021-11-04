from __future__ import annotations

import collections
import pprint


def signature(word: str) -> str:
    """Return a word sorted
    >>> signature("test")
    'estt'
    >>> signature("this is a test")
    '   aehiisssttt'
    >>> signature("finaltest")
    'aefilnstt'
    """
    return "".join(sorted(word))


def anagram(my_word: str) -> list[str]:
    """Return every anagram of the given word
    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return word_bysig[signature(my_word)]


with open("words.txt") as f:
    word_list = sorted(list({word.strip().lower() for word in f}))

word_bysig = collections.defaultdict(list)
for word in word_list:
    word_bysig[signature(word)].append(word)

if __name__ == "__main__":
    all_anagrams = {word: anagram(word) for word in word_list if len(anagram(word)) > 1}

    with open("anagrams.txt", "w") as file:
        file.write("all_anagrams = \n ")
        file.write(pprint.pformat(all_anagrams))
