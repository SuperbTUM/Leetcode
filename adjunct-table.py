# [[0,1],[1,2]]
# The adjunct table stores the set of the rear node of each current node

class AdjacencyTable:
    def __init__(self, n):
        # self.adj = [set()] * n is not a correct expression
        self.adj = [set() for _ in range(n)]
        self.in_degrees = [0] * n
        self.n = n

    def build(self, example):
        for first, second in example:
            # assuming first -> second
            self.adj[first].add(second)
            # The rear node needs one more pre-condition (precursor node) to be found
            self.in_degrees[second] += 1

    def find_path(self):
        stack = []
        for i, degree in enumerate(self.in_degrees):
            if not degree:
                # no precursor found -> node could be found immediately, consider it as the beginning
                stack.append(i)
        cnt = 0
        while stack:
            node = stack.pop(0)
            # node = stack.pop() is slower because a queue is faster
            cnt += 1
            for cont in self.adj[node]:
                # one effective rear node found
                self.in_degrees[cont] -= 1
                # All prerequisites met, node found
                if self.in_degrees[cont] == 0:
                    stack.append(node)
        return self.n == cnt


# The core idea of DFS is to judge if a circle exists inside the adjunct table
# Not sure if an inverse one is better
class AdjacencyTableDFS:
    def __init__(self, n):
        self.adj = [set() for _ in range(n)]
        self.in_degrees = [0] * n
        self.n = n
        self.visited = [0] * n  # three status : 0 -- not visited; 1 -- visited and traverse completed;
        # 2 -- visited and traverse not completed, which means a circle exists

    def build(self, example):
        for first, second in example:
            # assuming first -> second
            self.adj[first].add(second)
            # The rear node needs one more pre-condition (precursor node) to be found
            self.in_degrees[second] += 1

    def find_circle(self):
        for i in range(len(self.adj)):
            if self._dfs(i, self.adj, self.visited):
                return False
            return True

    def _dfs(self, i, adj, visited):
        # stop condition
        if visited[i] == 2:
            return True
        if visited[i] == 1:
            return False
        visited[i] = 2
        for cont in adj[i]:
            if self._dfs(cont, adj, visited):
                return True
        visited[i] = 1
        return False

