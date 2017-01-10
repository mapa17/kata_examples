############
#
#   Trying to solve
#   https://www.codewars.com/kata/getting-along-with-integer-partitions/train/python
#
############

from pudb import set_trace as st

import sys
from functools import reduce
import numpy as np

# Use this dictionary to hash results and reuse them 
sum_ones_memory = {}
def sum_ones(part, prod):
    """
    Sum up all 1's in a list, and calculate the product sum
    Return the original list and the summed
    If the list only contains one 1, dont calculate the sum

    >>> sum_ones((1, 1, 2), 1*1*2)
    [(1, 1, 2), (2, 2)], [2, 4]
    >>> sum_ones((1, 2), 2)
    [(1, 2)], [2]
    >>> sum_ones((2, ), 2)
    [(2,)], [2]
    """
    if part in sum_ones_memory:
        partList, prodList = sum_ones_memory[part]
    else:
        n1 = part.count(1)
        partList = [part]
        prodList = [prod]
        if n1 > 1:
            npart = tuple(filter(lambda x: x != 1, part))
            npart = (n1,) + npart
            partList.append(npart)
            prodList.append(prod * n1)

        sum_ones_memory[part] = partList, prodList
    return partList, prodList

def add_number(partitions, number):
    # Add to each list in partitions add 1
    prods = partitions.values()
    nKeys = [(1,) + x for x in partitions.keys()]

    # apply sum_ones on each partition, and add results to partitions

    # Done use reduce, the continues list creation is just too slow
    #partitions = reduce(lambda acc, x: acc + sum_ones(x), partitions, [])
    newParts = []
    newProds = []
    for part, prod in zip(nKeys, prods):
        npart, nprod = sum_ones(part, prod)
        newParts.extend(npart)
        newProds.extend(nprod)

    # Remove duplicates
    return dict(zip(newParts, newProds))

def partitions(value, show_progress=False):
    p = {(1,): 1}
    for num in range(2, value+1):
        p = add_number(p, num)
        if show_progress:
            print(('%d' % num) + '.'*num)
    return p

def part(n, show_progress=False):
    # Get partitions as list of tuples
    parts = partitions(n, show_progress=show_progress)

    #products = set(map(lambda x: np.prod(x), parts))
    # Only count unique products
    filtered_products = list(set(parts.values()))
    filtered_products.sort()

    return format('Range: %d Average: %.2f Median: %.2f' % 
        (filtered_products[-1]-filtered_products[0], np.mean(filtered_products), np.median(filtered_products)))


if __name__ == "__main__":
    try:
        n = [int(x) for x in sys.argv[1:]]
    except Exception:
        n = 10

    for num in n:
        print(part(num, show_progress=False))
        #print(part(num, show_progress=True))