def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    # version 1
    # if keys is longer than vals, add None to extend vals
    # if len(keys) > len(values):
    # amount_to_extend = len(keys) - len(values)

    # values += [None] * amount_to_extend

    # mergedDic = {}
    # mergedDic.update(zip(keys, values))

    # return mergedDic

    extended_values = values + [None] * max(0, len(keys) - len(values))
    return dict(zip(keys, extended_values))

