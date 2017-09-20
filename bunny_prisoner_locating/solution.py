def answer(x, y):
    layer = x + y - 1
    pre_total = layer * (layer - 1) // 2
    return str(pre_total + x)


print(answer(1, 1) == "1")
print(answer(3, 2) == "9")
print(answer(2, 3) == "8")
print(answer(5, 10) == "96")
