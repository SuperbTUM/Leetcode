from typing import List
# when you stand on top of the mountain with the odd index, look right, otherwise look left
# the function returns the sum of the mountains you will see by standing on each one.


def view_mountains(mountains: List[int]) -> int:
    if len(mountains) < 2:
        return 0
    m = len(mountains)
    dp_left = [1] * m
    for i in range(1, m):
        for j in range(i):
            if mountains[i] < mountains[j]:
                dp_left[i] = max(dp_left[i], dp_left[j] + 1)
    for ii in range(1, m):
        if dp_left[ii] < dp_left[ii-1]:
            dp_left[ii] = dp_left[ii-1]
    dp_left.insert(0, 0)
    dp_right = [1] * m
    for i in range(m-2, -1, -1):
        for j in range(m-1, i-1, -1):
            if mountains[i] < mountains[j]:
                dp_right[i] = max(dp_right[i], dp_right[j] + 1)
    for jj in range(1, m):
        if dp_right[jj] < dp_right[jj-1]:
            dp_right[jj] = dp_right[jj-1]
    dp_right.append(0)
    print(dp_left)
    print(dp_right)
    res = 0
    for k in range(m):
        if k & 1:
            res += dp_right[k+1]
        else:
            res += dp_left[k]
    return res


if __name__ == '__main__':
    mountains = [6, 5, 5, 4]
    print(view_mountains(mountains))