"""
To get the fewest steps, use BFS to traverse the maze.
Each step, there are possible four direction (up, down, left, right)
Since we can break the wall once, use a bool wallBefore to memory this status
"""


def answer(maze):
    h = len(maze)
    w = len(maze[0])

    visit = set()
    step = 1
    queue = [(0, 0, 0)]
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j, wallBefore = queue.pop(0)
            # Reach the end
            if i == h - 1 and j == w - 1:
                return step
            # The position with status is visited, do nothing
            if (i, j, wallBefore) in visit:
                continue
            # The position is a wall and we have broken the other wall before, do nothing
            if wallBefore & maze[i][j]:
                continue
            # Record the position and status
            visit.add((i, j, wallBefore | maze[i][j]))
            # Add next positions into the queue
            if i < h - 1:
                queue.append([i+1, j, wallBefore | maze[i][j]])
            if j < w - 1:
                queue.append([i, j+1, wallBefore | maze[i][j]])
            if i > 0:
                queue.append([i-1, j, wallBefore | maze[i][j]])
            if j > 0:
                queue.append([i, j-1, wallBefore | maze[i][j]])
        step += 1
    return step

if __name__ == "__main__":
    maze = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    print(answer(maze) == 7)

    maze = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    print(answer(maze) == 11)
