class MFS:
    def __init__(self):
        self.father = {}

    def add(self, node):
        if node not in self.father:
            self.father[node] = None

    def merge(self, node1, node2):
        root1, root2 = self._find(node1), self._find(node2)

        if root1 != root2:
            self.father[root1] = root2

    def _is_connected(self, node1, node2):
        if self._find(node1) == self._find(node2):
            return True
        return False

    def _find(self, node):
        if not self.father[node]:
            return node

        while self.father[node]:
            node = self.father[node]
        return node

    def zip_tree(self, x):
        node = x
        if not self.father[node]:
            return
        while self.father[node]:
            node = self.father[node]
        # 得到 root

        while x != node:
            tmp = self.father[x]
            self.father[x] = node
            x = tmp


if __name__ == '__main__':
    merge_find_tree = MFS()
