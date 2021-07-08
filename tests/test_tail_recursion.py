from typing import List

from tail_recursion import tail_recursive
from tail_recursion import TailRecursion

def test_version():

    @tail_recursive
    def cum_sum(xs: List[int], sums: List[int], cur_sum: int):
        if not xs:
            # all of xs is consumed, returning the result, i.e. sums.
            # this will terminate the whole function.
            return sums
        else:
            # consume the head of the list
            h = xs[0]
            t = xs[1:]
            cur_sum += h
            sums.append(cur_sum)

            # this return is semantically equivalently to:
            #     return cum_sum(t, sums, cur_sum)
            # the function call is replaced with a TailRecursion instance
            # to avoid overflow the stack, or by-pass the recursion limit
            return TailRecursion(t, sums, cur_sum)

    assert cum_sum([2, 3, 5, 7, 11], [], 0) == [2, 5, 10, 17, 28]
