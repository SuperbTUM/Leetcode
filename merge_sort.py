from typing import List


def mergesort(nums, left, right, temp, indexes, res):
    mid = left + (right - left) >> 1
    mergesort(nums, left, mid, indexes, res)
    mergesort(nums, mid+1, right, indexes, res)
    if nums[indexes[mid]] <= nums[indexes[mid+1]]:
        return
    merge(nums, left, right, mid, temp, indexes, res)


def merge(nums, left, right, mid, temp, indexes, res):
    temp[left:right+1] = indexes[left:right+1]
    ll = left
    rr = mid + 1
    for k in range(left, right+1):
        if ll > mid:
            indexes[k] = temp[rr]
            rr += 1
        elif rr > right:
            indexes[k] = temp[ll]
            ll += 1
            res[indexes[k]] += right - mid
        elif nums[temp[ll]] < nums[temp[rr]]:
            indexes[k] = temp[ll]
            ll += 1
            res[indexes[k]] += (rr - mid - 1)
        elif nums[temp[ll]] > nums[temp[rr]]:
            indexes[k] = temp[rr]
            rr += 1

        else:
            pass


def myPow(self, x: float, n: int) -> float:
    num = [1]
    res = []

    def itr(num, i, n, x, res):
        print(i)
        if i == n:
            res = num[:]
            print(res)
            return

        itr([nu * x for nu in num], i + 1, n, x, res)

    itr(num, 0, n, x, res)
    return res

import sys
recur_l = sys.getrecursionlimit()