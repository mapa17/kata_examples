def tail_swap(strings):
    """
    >>> tail_swap(['abc:123', 'cde:456'])
    ['abc:456', 'cde:123']
    >>> tail_swap(['a:12345', '777:xyz'])
    ['a:xyz', '777:12345']
    >>> tail_swap(['a:12345', '777:xyz', 'abc:123', 'ABC:789'])
    ['a:xyz', '777:12345', 'abc:789', 'ABC:123']
    """
    nlist = []
    fragments = iter([s.split(':') for s in strings])
    for a, b in zip(fragments, fragments):
        nlist.append(a[0] + ':' + b[1])
        nlist.append(b[0] + ':' + a[1])
    return nlist
