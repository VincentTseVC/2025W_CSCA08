def count_vowels(L: list[str]) -> int:
    """Return the number of total vowels in L.

    >>> count_vowels(['Vincent', 'I like programming', 'vc'])
    8
    """
    count = 0
    for s in L:
        for ch in s:
            if ch in 'aeiouAEIOU':
                count += 1
    return count


print(count_vowels(['Vincent', 'I like programming', 'vc']))



def count_word_vowels(L: list[str]) -> list[int]:
    """Return a list that contains the number of vowels of each
    strings in L.

    >>> count_word_vowels(['Vincent', 'I like programming', 'vc'])
    [2, 6, 0]
    """
    result = []
    for s in L:
        count = 0 # Reset
        for ch in s:
            if ch in 'aeiouAEIOU':
                count += 1
        result.append(count)

    return result


print(count_word_vowels(['Vincent', 'I like programming', 'vc']))