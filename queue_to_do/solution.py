"""
Use bulk_xor to speed up xor calculate.
Let f(x) = 1 ^ 2 ^ 3 ^ ... ^ x
Then, xor all integers in the range from m to n = f(n) ^ f(m-1)
"""


def answer(start, length):

    def bulk_xor(m, n):
        # f(x) = 1 ^ 2 ^ 3 ^ ... ^ x
        # bulk_xor(m, n) = m ^ m+1 ^ m+2 ... ^ n = f(n) ^ f(m-1)
        m -= 1
        f_m = [m, 1, m + 1, 0][m % 4]
        f_n = [n, 1, n + 1, 0][n % 4]
        return f_m ^ f_n

    xor = 0
    for i in range(length):
        xor ^= bulk_xor(start, start + length - i - 1)
        start += length

    return xor


print(answer(0, 3))
print(answer(17, 4))
