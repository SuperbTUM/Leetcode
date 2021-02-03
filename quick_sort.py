from typing import List
from random import randint


class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    @property
    def size(self):
        return len(self.nums)

    def quick_sort(self, left: int, right: int):
        if left < right:
            mid = self._partition(left, right)
            self.quick_sort(left, mid - 1)
            self.quick_sort(mid + 1, right)
        else:
            return

    def _partition(self, left: int, right: int) -> int:
        index = randint(left, right)
        # put this to the very left?
        self.nums[index], self.nums[left] = self.nums[left], self.nums[index]
        x = self.nums[left]
        # then the referred value lies on the left
        j = left  # store the position of x
        for i in range(left + 1, right + 1):
            # right to the referred value, if it is smaller, pointer j increased by 1
            if self.nums[i] < x:
                j += 1
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        # put x into the right place
        self.nums[j], self.nums[left] = self.nums[left], self.nums[j]
        return j


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    qs = QuickSort(nums)
    qs.quick_sort(0, qs.size - 1)
    print(qs.nums)
    assert qs.nums == [1, 2, 3, 4, 5, 6]
