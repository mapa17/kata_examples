def tail_swap(strings):
    """
    >>> tail_swap(['abc:123', 'cde:456'])
    ['abc:456', 'cde:123']
    >>> tail_swap(['a:12345', '777:xyz'])
    ['a:xyz', '777:12345']
    """
    h1, t1 = strings[0].split(':')
    h2, t2 = strings[1].split(':')

    return [h1 + ':' + t2, h2 + ':' + t1]
