# -*- coding:utf-8 -*-
# This self-defined class mixes the classic heap sort method with the searching of kth largest/smallest.

class Heappp:
    def __init__(self, smallest=True, kth_largest=False):
        self.array = []
        self.smallest = smallest
        self.kth_largest = kth_largest
        if self.kth_largest:
            self.array_len_k = []

    def _smaller(self, a, b):
        return a > b if self.smallest else b > a

    def _swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def _swap_4_kth_smallest(self, a, b):
        self.array_len_k[a], self.array_len_k[b] = self.array_len_k[b], self.array_len_k[a]

    def _sift_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._smaller(self.array[index], self.array[parent]):
                break
            self._swap(index, parent)
            index = parent

    def _sift_up_4_kth_smallest(self, index):
        while index:
            parent = (index - 1) // 2
            if self._smaller(self.array_len_k[index], self.array_len_k[parent]):
                break
            self._swap_4_kth_smallest(index, parent)
            index = parent

    @property
    def size(self):
        return len(self.array)

    def insert(self, num):
        self.array.append(num)
        self._sift_up(self.size - 1)

    def maintain_k_array(self, num, k=1):
        # default k: 1
        if self.kth_largest:
            if len(self.array_len_k) < k:
                self.array_len_k.append(num)
            else:
                if (self.smallest and num < self.array_len_k[-1])\
                           or (not self.smallest and num > self.array_len_k[-1]):
                    self.array_len_k[-1] = num

            self._sift_up_4_kth_smallest(len(self.array_len_k) - 1)
        else:
            print("The function is not enabled. Check the value of kth_largest.\n")

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

    def kth_smallest(self, k=1):
        if self.kth_largest:
            if len(self.array_len_k) < k:
                print("Value is not available.\n")
                return
            else:
                return self.array_len_k[-1]
        else:
            print("The function is not enabled. Check the value of kth_largest.\n")


def solution():
    heap = Heappp(smallest=False, kth_largest=True)
    ls = [2, 7, 4, 1, 8, 1]
    k = 2
    for ele in ls:
        heap.insert(ele)
        heap.maintain_k_array(ele, k)
        #print(heap.array)
    print("The {}st/nd/rd/th smallest/largest in the list is {}".format(k, heap.kth_smallest(k)))
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