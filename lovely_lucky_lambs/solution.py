"""
Max: #(fib number list)

Min: #(power of 2 list)
     last element a[n] can be any number between (a[n-1] + a[n-2], a[n-1] * 2)
"""


def answer(total_lambs):

    # Power of 2 list
    min_v = -1
    n = total_lambs + 1
    while n:
        n >>= 1
        min_v += 1
    # last element can smaller than 2 ** min_v
    # but still need to follow rules
    x = 1 << min_v
    if (x + x // 2 + x // 4 - 1) <= total_lambs:
        min_v += 1

    # Fib list
    max_v = 1
    x, y, n = 1, 1, total_lambs - 1
    while n > 0:
        x, y = y, x + y
        n -= y
        max_v += 1

    return max_v - min_v

if __name__ == "__main__":
    for i in range(15):
        print(i, answer(i))
