import sys

"""
Program to count the number of tilings of a rectangular m x n board
with dominoes.

Written for the Problem Solving event at FCL 2017
"""

def boolarray_to_mask(arr):
    # arr = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    mask = []
    for row in arr:
        num = 0
        for i in range(len(row)):
            if row[i]:
                num |= (1 << i)
        mask.append(num)
    return tuple(mask), len(arr[0])

def tilings_mask(bool_array):
    ''' counts the number of tilings given boolean array representing board '''
    return recurse(*boolarray_to_mask(bool_array))

def tilings(m, n):
    ''' counts the number of tilings of a rectangle m x n'''

    if m*n&1:
        return 0
    m, n = max(m, n), min(m, n)
    mask = tuple([(1<<n) - 1] * m)
    return recurse(mask, n)

memo = {}
def recurse(mask, columns):
    if mask in memo:
        return memo[mask]
    if mask == (): # empty
        return 1

    ret = 0
    new_mask1, new_mask2 = list(mask), list(mask)
    curr = 0
    # find the first place where domino can be placed
    while not mask[0] & (1 << curr):
        curr += 1

    # try placing horizontal domino
    if mask[0] & (1 << (curr + 1)):
        new_mask1[0] &= ~(1 << curr)
        new_mask1[0] &= ~(1 << (curr + 1))
        while len(new_mask1) > 0 and new_mask1[0] == 0:
            del new_mask1[0]
        ret += recurse(tuple(new_mask1), columns)

    # try placing vertical domino
    if len(mask) > 1 and mask[1] & (1 << curr):
        new_mask2[0] &= ~(1 << curr)
        new_mask2[1] &= ~(1 << curr)
        while len(new_mask2) > 0 and new_mask2[0] == 0:
            del new_mask2[0]
        ret += recurse(tuple(new_mask2), columns)
    memo[mask] = ret
    return ret

# example use of tilings of a board with holes
# print(tilings_mask([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))

print('Insert space separated dimensions of the board: ')
inp = sys.stdin.readline()
m, n = map(lambda x: int(x.strip()), inp.strip().split())
print('The number of tilings of a {:d} x {:d} board is: {:d}'.format(m, n, tilings(m, n)))
