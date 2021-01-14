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
            # let us consider another solution
            # self.in_degrees[first] += 1
            # this means to access the precursor node, you need to reach all its rear node
            # In the scenario of course study, consider the precursor node as the course you would like to enroll
            # The content of its rear node is the pre-course you have to take in advance
            # In the case of self.in_degrees[second] += 1
            # this means you have another course to take when this pre-course is finished
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
            # The reason why a queue is faster here is that the main idea of this method is BFS
            cnt += 1
            # The way of defining self.is_degrees deeply affects the logic here
            # considering another option, the traverse logic needs to focus on the key of the adjunct table
            # rather than the value
            # for i in range(len(self.adj)):
            #     if node in self.adj[i]:
            #         self.in_degrees[i] -= 1
            #         if self.in_degrees[i] == 0:
            #             stack.append(i)
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

