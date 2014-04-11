#!/usr/bin/env python
""" Pisano period.
"""

__author__ = 'Andrew Rowles'
__email__ = 'andrew@rowles.io'

# The list length of the Fibonacci Sequence
FIB_LIM = 3000

MODULO = 10


def F():
    """ Generate sequence of Fibonacci numbers.
    """
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a


def fibonacci_modulo(lim=FIB_LIM, mod=MODULO):
    """ Generate sequence of Fibonacci numbers modulo mod.

    Parameters
    ----------
    lim: integer
        The number of Fibonacci numbers to generate.
    mod: integer
        The modulo.

    Return a list of the Fibonacci numbers modulo.

    """
    fibs = []
    fib_seq = F()

    for n in range(lim):
        fibs.append(next(fib_seq) % mod)

    return fibs


def find_period(l):
    """ Finds the period of list of numbers.

    Parameters
    ----------
    l: integer[]
        The sequence of numbers.

    Return
    ------
    steps: integer
        The period.

    Returns None, if no period is found.

    """

    steps = 1

    for i in xrange(1, len(l)):
        if l[i] == l[0]:
            if l[:i] == l[i:i+i]:
                return steps

        steps += 1

    return None


def pisano_period(mod=MODULO, lim=FIB_LIM, console=False):
    """ Calculate the Pisano period.

    Parameters
    ----------
    mod: integer
        ...
    lim: integer
        ...

    """

    # Sequence of Fibonacci numbers modulo mod
    mod_fibs = fibonacci_modulo(mod=mod, lim=lim)

    # Find the Pisano period
    period = find_period(mod_fibs)

    if console and period:
        print "Pisano Period modulo %s" % mod
        print 'Period Length: %s' % find_period(mod_fibs)
        print mod_fibs[:period]

    return period


def main():
    pisano_period(mod=400, console=True)


main()