"""
Generate prime table and then join them together into a single string.
"""


def answer(n):
    table = [True] * 20220
    table[0] = table[1] = False
    for i in range(2, 20220):
        if table[i]:
            for j in range(i + i, 20220, i):
                table[j] = False
    prime_str = "".join([str(i) for i in range(1, 20220) if table[i]])
    return prime_str[n: n + 5]

if __name__ == "__main__":
    print(answer(5000))
