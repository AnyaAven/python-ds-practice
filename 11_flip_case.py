def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_str = ""

    for ltr in phrase:
        if ltr == to_swap.lower() or ltr == to_swap.upper():
            new_str += ltr.swapcase()
        else:
            new_str += ltr

    return new_str


print(flip_case("aaahHHHHShdhshhs", "h"))