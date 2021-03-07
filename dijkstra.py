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
    heapq.heapify(q, [(weight, x, y)])
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
            if 0 <= direction[0] < m and 0 <= direction[1] < n and \
                    weight[lx * n + ly] + abs(w - grid[direction[0]][direction[1]]) < \
                    weight[direction[0] * n + direction[1]]:
                weight[direction[0] * n + direction[1]] = weight[lx * n + ly] + (w -
                                                                                 grid[direction[0]][direction[1]])
                heapq.heappush(q, (weight[direction[0] * n + direction[1]], direction[0], direction[1]))

    return weight[m * n - 1]


def dijk_weighted_graph(self, n: int, edges: List[List[int]]) -> int:
    node = collections.defaultdict(list)
    wd = collections.defaultdict(list)
    for prev, nex, wgt in edges:
        node[prev].append(nex)
        wd[prev].append(wgt)
        node[nex].append(prev)
        wd[nex].append(wgt)

    # 先求所有节点到节点n的最短距离
    # Dijkstra
    def dijk(start):
        if start == n:
            return 0
        weight = [0] + [inf] * (n)
        q = [(weight[0], start)]
        visited = set()
        while q:
            w, curr = heapq.heappop(q)
            if curr in visited:
                continue
            if curr == n:
                break
            visited.add(curr)
            # directions available
            directions = node[curr]

            for i, direction in enumerate(directions):
                if wd[curr][i] + w < weight[direction]:
                    weight[direction] = w + wd[curr][i]
                    heapq.heappush(q, (weight[direction], direction))
            # print(q)
        return weight[-1]

    tmp = []
    for i in range(1, n+1):            
        tmp.append(dijk(i))
    print(tmp)
