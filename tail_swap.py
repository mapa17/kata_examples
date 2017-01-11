def tail_swap(strings):
    """
    >>> tail_swap(['abc:123', 'cde:456'])
    ['abc:456', 'cde:123']
    >>> tail_swap(['a:12345', '777:xyz'])
    ['a:xyz', '777:12345']
    """
    a, b = strings

    ai = a.index(':')
    bi = b.index(':')

    A = a[:ai] + ':' + b[bi+1:]
    B = b[:bi] + ':' + a[ai+1:]

    return [A, B]
