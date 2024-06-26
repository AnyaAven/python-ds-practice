from collections import Counter

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # RETURN key of highest value
    freqs = Counter(nums)
    return freqs.most_common(1)[0][0] #[0] to enter the list and another [0] to enter the tuple
