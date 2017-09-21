def answer(dimensions, captain_position, badguy_position, distance):
    cx, cy = captain_position
    sqr_dist = distance ** 2

    if captain_position == badguy_position:
        return 0

    def get_mirrored(node):
        yield (node[0], node[1] - 2 * (node[1] - dimensions[1]))
        yield (node[0], -node[1])
        yield (node[0] - 2 * (node[0] - dimensions[0]), node[1])
        yield (-node[0], node[1])

    def get_slope(dx, dy):
        if dx == dy == 0:
            return (0, 0)
        tx, ty = abs(dx), abs(dy)
        while ty:
            tx, ty = ty, tx % ty
        return (dx // tx, dy // tx)

    def get_all_mirror(node):
        prev = mirrors = set([(node[0], node[1])])
        while True:
            new_mirrors = set()
            for node in prev:
                for tmp in get_mirrored(node):
                    if (cx - tmp[0]) ** 2 + (cy - tmp[1]) ** 2 > sqr_dist:
                        continue
                    new_mirrors.add(tmp)
            new_mirrors -= mirrors
            if not new_mirrors:
                break
            mirrors |= new_mirrors
            prev = new_mirrors
        return mirrors

    bads = get_all_mirror(badguy_position)
    caps = get_all_mirror(captain_position)
    caps_slope = {}

    for x, y in caps:
        dx = cx - x
        dy = cy - y
        dist = dx ** 2 + dy ** 2
        slope = get_slope(dx, dy)
        if dist <= caps_slope.get(slope, sqr_dist):
            caps_slope[slope] = dist

    ans = set()
    for x, y in bads:
        dx = cx - x
        dy = cy - y
        dist = dx ** 2 + dy ** 2
        slope = get_slope(dx, dy)
        if dist <= caps_slope.get(slope, sqr_dist):
            ans.add(slope)
    return len(ans)

if __name__ == "__main__":
    print(0, answer((3, 2), (1, 1), (1, 1), 4))
    print(7, answer((3, 2), (1, 1), (2, 1), 4))
    print(9, answer((300, 275), (150, 150), (185, 100), 500))
    print(27, answer((2, 5), (1, 2), (1, 4), 11))
