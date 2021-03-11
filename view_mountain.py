from typing import List
# when you stand on top of the mountain with the odd index, look right, otherwise look left
# the function returns the sum of the mountains you will see by standing on each one.


def view_mountains(mountains: List[int]) -> int:
    if len(mountains) < 2:
        return 0
    res = 0
    # monostack
    right = []
    for j in range(len(mountains)-1, 1, -1):
        if not right or mountains[j] < right[-1]:
            right.append(j)
    same_with_curr = [mountains[index] for index in right].count(mountains[1])
    res += len(right) - same_with_curr

    left = []
    if len(mountains) & 1:
        last_even_index = len(mountains) - 1
    else:
        last_even_index = len(mountains) - 2
    for k in range(last_even_index):
        if not left or mountains[k] > left[-1]:
            left.append(k)
    same_with_curr = [mountains[index] for index in left].count(mountains[last_even_index])
    res += len(left) - same_with_curr

    for i in range(len(mountains)):
        if i & 1 and i > 1:  # look right
            while i+1 in right or i in right:
                right.pop()
            same_with_curr = [mountains[index] for index in right].count(mountains[i])
            res += len(right) - same_with_curr

    for m in range(last_even_index-2, -1, -1):
        if m & 1 == 0:
            while m+1 in left or m in left:
                left.pop()
            same_with_curr = [mountains[index] for index in left].count(mountains[m])
            res += len(left) - same_with_curr

    return res


if __name__ == '__main__':
    mountains = [6, 5, 5, 4]
    print(view_mountains(mountains))
