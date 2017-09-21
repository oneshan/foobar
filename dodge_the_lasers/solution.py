# beatty sequence sum
# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
from decimal import Decimal, getcontext
getcontext().prec = 101
sqrt2m1 = Decimal(2).sqrt() - 1


def answer(str_n):
    n = long(str_n)

    def s(n):
        if n == 1:
            return 1
        if n < 1:
            return 0
        n1 = long(sqrt2m1 * n)
        return n * n1 + n * (n + 1) // 2 - n1 * (n1 + 1) // 2 - s(n1)

    return str(s(n))


if __name__ == "__main__":
    print("4208", answer("77"))
    print("19", answer("5"))
