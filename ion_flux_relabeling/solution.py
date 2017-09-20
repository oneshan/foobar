def answer(h, q):
    ans = [-1] * len(q)
    max_v = (1 << h) - 1

    def getPid(h, target, bias):
        max_v = (1 << h) - 1
        max_hv = max_v // 2
        # target == left node
        if target == max_hv + bias:
            return max_v + bias
        # target == right node
        elif target == (max_hv << 1) + bias:
            return max_v + bias
        # target in left subtree
        elif target < max_hv + bias:
            return getPid(h - 1, target, bias)
        # target in right subtree
        else:
            return getPid(h - 1, target, bias + max_hv)

    for idx, elem in enumerate(q):
        if elem < max_v:
            ans[idx] = getPid(h, elem, 0)

    return ans

print(answer(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(answer(3, [7, 3, 5, 1]))
print(answer(5, [19, 14, 28]))
