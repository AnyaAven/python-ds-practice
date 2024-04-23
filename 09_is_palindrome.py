def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    formattedPhrase = phrase.lower().replace(" ", "")
    formattedPhraseReverse = formattedPhrase[::-1]

    # NOTE: return line 27 (instead of if)
    if formattedPhrase == formattedPhraseReverse:
        return True
    return False
