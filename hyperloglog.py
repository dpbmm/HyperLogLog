#! /usr/bin/env python
# hyperloglog.py
# 20150609

import zlib
from scipy import stats

def generate_multiset(lower_bound, upper_bound, number_of_uniques, number_of_items):
    """Generate multiset
    Generate a set of "number_of_uniques" numbers
    Generate a list of "number_of_items" final numbers with unique numbers appearing multiple times
    Shuffle the list and return it
    """
    pass

alphas = {
    16: 0.673,
    32: 0.696,
    64: 0.709
}

def alpha(m):
    if m in alphas:
        return alphas[m]
    else:
        return 0.7213 / (1 + (1.079 / m))

def harmonic_mean(registers):
    return 1 / sum([2 ** (-register) for register in registers if register > 0])

def hyperloglog(multiset, b = 5):
    """Compute the estimate of the number of unique elements in multiset
    """
    m = 2 ** b
    registers = [0] * (m + 1)

    for item in multiset:
        x = zlib.adler32(str(item))
        bin_x = bin(x)[2:] # Truncating 0b
        leftbits = bin_x[:b]
        j = int("0b" + leftbits, 2) + 1

        rightbits = bin_x[b:]
        w = rightbits

        p = w.find("1") + 1
        print("w = ", w)
        print("p = ", p)

        registers[j] = max(registers[j], p)

    print(registers)
    print(harmonic_mean(registers))
    print(stats.hmean(registers))

    return alpha(m) * (m ** 2) * harmonic_mean(registers)

print (hyperloglog([1, 1, 2], 4))
