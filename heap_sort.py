# -*- coding:utf-8 -*-
class Heappp:
    def __init__(self, smallest=True):
        self.array = []
        self.smallest = smallest

    def _smaller(self, a, b):
        return a > b if self.smallest else b > a

    def _swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def _sift_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._smaller(self.array[index], self.array[parent]):
                break
            self._swap(index, parent)
            index = parent

    @property
    def size(self):
        return len(self.array)

    def insert(self, num):
        self.array.append(num)
        self._sift_up(self.size - 1)

    def pop(self):
        top = self.array[0]
        self._swap(0, -1)
        self.array.pop()
        self._sift_down(0)
        return top

    def _sift_down(self, index):
        while 2 * index + 1 < self.size:
            parent = index
            left_children = 2 * index + 1
            right_children = 2 * index + 2

            if not self._smaller(self.array[parent], self.array[left_children]):
                parent = left_children
            if right_children < self.size and not self._smaller(self.array[parent], self.array[right_children]):
                parent = right_children
            if parent == index:
                break
            self._swap(parent, index)


def solution():
    heap = Heappp(smallest=False)
    ls = [2, 7, 4, 1, 8, 1]
    for ele in ls:
        heap.insert(ele)
        #print(heap.array)
    while heap.size > 1:
        x, y = heap.pop(), heap.pop()
        if x != y:
            heap.insert(x - y)
        #print(heap.array)
    if heap.size:
        return heap.array[0]
    return 0


if __name__ == '__main__':
    print(solution())
