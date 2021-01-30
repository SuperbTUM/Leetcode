import heapq
from typing import List


# we can absolutely use heap as priority queue
def dijk(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    # the graph should start like this
    weight = [0] + [inf] * (m * n - 1)
    x = 0
    y = 0
    # when you read the document
    # there is no need for initialization
    # thanks to heapify module
    heapq.heapify([(weight, x, y)])
    visited = set()
    # then it is time to do something cool
    # remember this is a min heap
    while q:

        w, lx, ly = heapq.heappop(q)
        if (lx, ly) in visited:
            continue
        if lx == m - 1 and ly == n - 1:
            break
        visited.add((lx, ly))
        # directions available
        directions = [(lx - 1, ly), (lx + 1, ly), (lx, ly + 1), (lx, ly - 1)]
        for direction in directions:
            if 0 < lx < m - 1 and 0 < ly < n - 1 and weight[direction[0] * n + direction[1]] + abs(grid[lx][ly] -
                                                                                                   grid[direction[0]][
                                                                                                       direction[1]]) < \
                    weight[lx * n + ly]:
                weight[lx * n + ly] = weight[direction[0] * n + direction[1]] + (grid[lx][ly] -
                                                                                 grid[direction[0]][direction[1]])
                heapq.heappush(q, (weight[lx * n + ly], direction[0], direction[1]))

    return weight[m * n - 1]
