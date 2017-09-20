"""
Suppose M > F, to hit (M, F), last state must be (M-F, F).

We can use Euclidean algorithm to calcualte the generations
from (M, F) down to (1, 1)

A simple case: (1, 1)-(2, 1)-(3, 1)-(3, 4)-(7, 4)
Impossible Case: gcd(M, F) != 1
"""


def answer(M, F):
    x, y = int(M), int(F)
    count = 0
    while y >= 1:
        if x < y:
            x, y = y, x
        x, y, q = y, x % y, x // y
        count += q
    return str(count - 1) if x == 1 else "impossible"


print(answer("4", "7"))
print(answer("2", "1"))
print(answer("3", "6"))
