def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_freqs = {}
    for letter in phrase:
        # letter_freqs[letter] = phrase.count(letter)  # NOTE: use get method

        val = letter_freqs.get(letter, 0)
        letter_freqs[letter] = val + 1

        # can be done in one line
        # letter_freqs[letter] = letter_freqs.get(letter, 0) + 1

    return letter_freqs
