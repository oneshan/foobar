def answer(banana_list):
    banana_list.sort(reverse=True)
    n = len(banana_list)

    def isLoop(x, y):
        z = x + y
        while y:
            x, y = y, y % x
        z //= x
        return (z & (z - 1)) != 0

    graph = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            if isLoop(banana_list[i], banana_list[j]):
                graph.setdefault(i, [])
                graph.setdefault(j, [])
                graph[i].append(j)
                graph[j].append(i)

    return maximum_matching(graph, n)


def maximum_matching(graph, size):
    exposed = list(range(size))
    nonmatch_e = set([(x, y) for x in graph for y in graph[x]])
    match_e = set()

    hasPath = True
    while hasPath:
        hasPath = False
        for start in exposed:
            visited = set()
            flag = False
            path = []
            u = start

            while True:
                visited.add(u)

                for v in graph.get(u, []):
                    if v in visited:
                        continue
                    if (not flag and (u, v) in nonmatch_e) or (flag and (u, v) in match_e):
                        path.append(u)
                        path.append(v)
                        break

                if not path:
                    break

                if path[-1] in exposed and path[-1] != start:
                    hasPath = True
                    for i in range(len(path) - 1):
                        if (path[i], path[i + 1]) in match_e:
                            match_e.remove((path[i], path[i + 1]))
                            match_e.remove((path[i + 1], path[i]))
                            nonmatch_e.add((path[i], path[i + 1]))
                            nonmatch_e.add((path[i + 1], path[i]))
                        else:
                            nonmatch_e.remove((path[i], path[i + 1]))
                            nonmatch_e.remove((path[i + 1], path[i]))
                            match_e.add((path[i], path[i + 1]))
                            match_e.add((path[i + 1], path[i]))
                    exposed.remove(path[0])
                    exposed.remove(path[-1])
                    break

                flag = not flag
                u = path.pop()

    return len(exposed)
