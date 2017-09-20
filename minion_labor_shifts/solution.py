from collections import Counter


def answer(data, n):
    if n == 0:
        return []
    if len(data) < n:
        return data
    c = Counter(data)
    return [d for d in data if c[d] <= n]


print(answer([1, 2, 3], 0) == [])
print(answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4])
print(answer([1, 2, 3], 6) == [1, 2, 3])
